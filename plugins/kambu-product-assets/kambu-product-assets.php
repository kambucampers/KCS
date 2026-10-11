<?php
/**
 * Plugin Name: Kambu Product Page Assets
 * Description: Loads the shared product-page stylesheet and script on any page whose content uses the .kpm product block. One copy, cached across every product page.
 * Version:     1.0.0
 * Author:      Kambu Campers
 * License:     GPL-2.0-or-later
 *
 * Install as a normal plugin (wp-content/plugins/kambu-product-assets/kambu-product-assets.php)
 * or drop it in wp-content/mu-plugins/ to have it always active.
 *
 * Put kambu-product.css and kambu-product.js in the same folder as this file.
 * Then delete the two marked <link> / <script src> lines from each page block.
 */

defined( 'ABSPATH' ) || exit;

const KAMBU_PRODUCT_MARKER = 'class="kpm"';

/** Does the post being rendered actually contain a product block? */
function kambu_product_page_has_block() {
	if ( ! is_singular() ) {
		return false;
	}
	$post = get_post();
	return $post && false !== strpos( (string) $post->post_content, KAMBU_PRODUCT_MARKER );
}

function kambu_product_assets_enqueue() {
	if ( ! kambu_product_page_has_block() ) {
		return;
	}

	$dir = plugin_dir_path( __FILE__ );
	$url = plugin_dir_url( __FILE__ );

	// filemtime means the browser picks up a new file the moment you upload one.
	$css = $dir . 'kambu-product.css';
	$js  = $dir . 'kambu-product.js';

	if ( file_exists( $css ) ) {
		wp_enqueue_style( 'kambu-product', $url . 'kambu-product.css', array(), (string) filemtime( $css ) );
	}
	if ( file_exists( $js ) ) {
		wp_enqueue_script( 'kambu-product', $url . 'kambu-product.js', array(), (string) filemtime( $js ), true );
	}
}
add_action( 'wp_enqueue_scripts', 'kambu_product_assets_enqueue' );
