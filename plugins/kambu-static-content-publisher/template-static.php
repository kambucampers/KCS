<?php
if (!defined('ABSPATH')) {
    exit;
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

$path = kambu_static_source_path($source);

get_header();

if ($path) {
    echo file_get_contents($path);
}

get_footer();