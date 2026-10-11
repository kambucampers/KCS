<?php
/**
 * Plugin Name: Kambu Static Content Publisher
 * Description: Publishes controlled HTML guide files as WordPress posts or pages without Gutenberg or wpautop rewriting the rendered HTML.
 * Version: 1.0.0
 * Author: Kambu Campers
 */

if (!defined('ABSPATH')) {
    exit;
}

define('KAMBU_STATIC_CONTENT_DIR', plugin_dir_path(__FILE__) . 'content/');
define('KAMBU_STATIC_META_SOURCE', '_kambu_static_source');
define('KAMBU_STATIC_META_TYPE', '_kambu_static_type');

function kambu_static_manifest() {
    static $manifest = null;

    if ($manifest !== null) {
        return $manifest;
    }

    $manifest_path = plugin_dir_path(__FILE__) . 'manifest.json';
    $manifest = file_exists($manifest_path) ? json_decode(file_get_contents($manifest_path), true) : array();

    return is_array($manifest) ? $manifest : array();
}

function kambu_static_template_slug() {
    return 'essential-blocks-fullwidth-template.php';
}

function kambu_static_source_path($source) {
    $source = basename((string) $source);
    $path = KAMBU_STATIC_CONTENT_DIR . $source;

    return is_file($path) ? $path : '';
}

function kambu_static_render_content($content) {
    if (!is_singular()) {
        return $content;
    }

    $post_id = get_the_ID();
    $source = get_post_meta($post_id, KAMBU_STATIC_META_SOURCE, true);
    $path = kambu_static_source_path($source);

    if (!$path) {
        return $content;
    }

    $raw_html = file_get_contents($path);

    return is_string($raw_html) ? $raw_html : $content;
}
add_filter('the_content', 'kambu_static_render_content', PHP_INT_MAX);

function kambu_static_template_include($template) {
    if (!is_singular()) {
        return $template;
    }

    $source = get_post_meta(get_queried_object_id(), KAMBU_STATIC_META_SOURCE, true);

    if (!$source) {
        $title = get_the_title(get_queried_object_id());

        foreach (kambu_static_manifest() as $item) {
            if (!empty($item['title']) && $item['title'] === $title) {
                $source = $item['source'];
                break;
            }
        }
    }

    if (!$source || !kambu_static_source_path($source)) {
        return $template;
    }

    $plugin_template = plugin_dir_path(__FILE__) . 'template-static.php';

    return is_file($plugin_template) ? $plugin_template : $template;
}
add_filter('template_include', 'kambu_static_template_include', PHP_INT_MAX);

function kambu_static_assign_template($post_id) {
    update_post_meta($post_id, '_wp_page_template', kambu_static_template_slug());
}

function kambu_static_sync_item($item, $status = 'draft') {
    $source = isset($item['source']) ? basename($item['source']) : '';
    $path = kambu_static_source_path($source);

    if (!$path || empty($item['title'])) {
        return new WP_Error('invalid_kambu_static_item', 'The manifest item is incomplete or its source file is missing.');
    }

    $type = (isset($item['type']) && $item['type'] === 'page') ? 'page' : 'post';
    if ($type === 'page' && empty($item['slug'])) {
        $front_page_id = (int) get_option('page_on_front');
        $existing = $front_page_id ? array($front_page_id) : array();
    } else {
        $existing = get_posts(array(
            'post_type' => array('post', 'page'),
            'post_status' => 'any',
            'meta_key' => KAMBU_STATIC_META_SOURCE,
            'meta_value' => $source,
            'numberposts' => 1,
            'fields' => 'ids',
        ));
    }

    $post_name = !empty($item['slug']) ? sanitize_title($item['slug']) : '';
    if (!$post_name && $existing) {
        $post_name = (string) get_post_field('post_name', (int) $existing[0]);
    }

    $postarr = array(
        'post_title' => sanitize_text_field($item['title']),
        'post_name' => $post_name,
        'post_status' => $status,
        'post_type' => $type,
        'post_content' => '[kambu_static_content]',
    );

    if ($existing) {
        $postarr['ID'] = (int) $existing[0];
    } else {
        $slug_match = get_page_by_path(sanitize_title($item['slug']), OBJECT, array('post', 'page'));

        if ($slug_match) {
            $postarr['ID'] = (int) $slug_match->ID;
            $postarr['post_status'] = $slug_match->post_status;
        } else {
            $title_match = get_posts(array(
                'post_type' => array('post', 'page'),
                'post_status' => 'any',
                'title' => sanitize_text_field($item['title']),
                'numberposts' => 1,
                'fields' => 'ids',
            ));

            if ($title_match) {
                $postarr['ID'] = (int) $title_match[0];
                $postarr['post_status'] = get_post_status($title_match[0]);
            }
        }
    }

    $post_id = wp_insert_post(wp_slash($postarr), true);

    if (is_wp_error($post_id)) {
        return $post_id;
    }

    update_post_meta($post_id, KAMBU_STATIC_META_SOURCE, $source);
    update_post_meta($post_id, KAMBU_STATIC_META_TYPE, $type);
    kambu_static_assign_template($post_id);

    return $post_id;
}

function kambu_static_admin_menu() {
    add_management_page(
        'Kambu Static Publisher',
        'Kambu Static Publisher',
        'manage_options',
        'kambu-static-publisher',
        'kambu_static_admin_page'
    );
}
add_action('admin_menu', 'kambu_static_admin_menu');

function kambu_static_admin_page() {
    if (!current_user_can('manage_options')) {
        return;
    }

    $manifest = kambu_static_manifest();
    $results = array();

    if (isset($_POST['kambu_static_sync']) && check_admin_referer('kambu_static_sync_all')) {
        $status = isset($_POST['kambu_static_status']) && $_POST['kambu_static_status'] === 'publish' ? 'publish' : 'draft';

        foreach ($manifest as $index => $item) {
            $type = isset($_POST['kambu_static_type'][$index]) && $_POST['kambu_static_type'][$index] === 'page' ? 'page' : 'post';
            $item['type'] = $type;
            $result = kambu_static_sync_item($item, $status);
            $results[] = is_wp_error($result) ? $result->get_error_message() : sprintf('%s #%d synced as %s.', $item['title'], $result, $type);
        }
    }
    ?>
    <div class="wrap">
        <h1>Kambu Static Content Publisher</h1>
        <p>These files render raw at the final content filter. Gutenberg and <code>wpautop</code> do not process the source HTML.</p>
        <?php if ($results) : ?>
            <div class="notice notice-success"><p><?php echo esc_html(implode(' ', $results)); ?></p></div>
        <?php endif; ?>
        <form method="post">
            <?php wp_nonce_field('kambu_static_sync_all'); ?>
            <table class="widefat striped">
                <thead><tr><th>Source</th><th>Title</th><th>Slug</th><th>Type</th></tr></thead>
                <tbody>
                <?php foreach ($manifest as $index => $item) : ?>
                    <tr>
                        <td><code><?php echo esc_html($item['source']); ?></code></td>
                        <td><?php echo esc_html($item['title']); ?></td>
                        <td><code><?php echo esc_html($item['slug']); ?></code></td>
                        <td>
                            <select name="kambu_static_type[<?php echo esc_attr($index); ?>]">
                                <option value="post" <?php selected(isset($item['type']) ? $item['type'] : 'post', 'post'); ?>>Post</option>
                                <option value="page" <?php selected(isset($item['type']) ? $item['type'] : 'post', 'page'); ?>>Page</option>
                            </select>
                        </td>
                    </tr>
                <?php endforeach; ?>
                </tbody>
            </table>
            <p>
                <label for="kambu_static_status"><strong>Sync status</strong></label>
                <select id="kambu_static_status" name="kambu_static_status">
                    <option value="draft">Create/update as drafts</option>
                    <option value="publish">Create/update as published</option>
                </select>
            </p>
            <p><button type="submit" name="kambu_static_sync" class="button button-primary">Sync all files</button></p>
        </form>
    </div>
    <?php
}

function kambu_static_shortcode() {
    return '';
}
add_shortcode('kambu_static_content', 'kambu_static_shortcode');
