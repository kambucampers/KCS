<?php
/**
 * Plugin Name:       Kambu Campers Safari Booking
 * Plugin URI:        https://kambucampers.com/
 * Description:       The Kambu Campers safari booking tool: 61 Kenya, Tanzania and cross-border safaris with live party-size pricing, child rates, add-ons and a bag checkout. Use the [kambu_safaris] shortcode. Optionally pass sheet="https://docs.google.com/...output=csv" to feed live prices from a published Google Sheet.
 * Version:           2.0.0
 * Author:            Kambu Campers
 * License:           GPL-2.0-or-later
 * Text Domain:       kambu-safaris
 */

if ( ! defined( 'ABSPATH' ) ) { exit; }

/**
 * [kambu_safaris]
 * [kambu_safaris sheet="https://docs.google.com/spreadsheets/d/e/XXXX/pub?gid=0&single=true&output=csv"]
 *
 * The fragment is a self-contained interface: all styles are scoped under
 * .kjs-root, all ids are unique to it, and the script is a single IIFE with
 * defensive DOM guards, so it coexists with any theme. Output is returned
 * from the shortcode directly and is NOT passed through KSES, which would
 * otherwise strip the svg/input elements the tool depends on.
 */
function kambu_safaris_shortcode( $atts ) {
	$atts = shortcode_atts( array( 'sheet' => '' ), $atts, 'kambu_safaris' );

	$file = plugin_dir_path( __FILE__ ) . 'fragment.html';
	if ( ! is_readable( $file ) ) {
		return '<p>The Kambu safari booking tool is missing its fragment.html file. Reinstall the plugin, or book via WhatsApp +254 769 103 670.</p>';
	}
	$html = file_get_contents( $file );

	$sheet = trim( (string) $atts['sheet'] );
	if ( $sheet && preg_match( '#^https://docs\.google\.com/#', $sheet ) ) {
		$html = str_replace(
			'id="kjsApp"',
			'id="kjsApp" data-sheet="' . esc_attr( $sheet ) . '"',
			$html
		);
	}
	return $html;
}
add_shortcode( 'kambu_safaris', 'kambu_safaris_shortcode' );

/**
 * [kambu_safaris_map] - the v2 "Waypoint" planner: country-first wizard,
 * clickable Kenya destination map, budget slider and sidebar slideshow.
 */
function kambu_safaris_map_shortcode() {
	$file = plugin_dir_path( __FILE__ ) . 'fragment-map.html';
	if ( ! is_readable( $file ) ) {
		return '<p>The Kambu safari planner is missing its fragment-map.html file. Reinstall the plugin, or book via WhatsApp +254 769 103 670.</p>';
	}
	return file_get_contents( $file );
}
add_shortcode( 'kambu_safaris_map', 'kambu_safaris_map_shortcode' );

/**
 * [kambu_safaris_browse] - the v3 "Registry" faceted catalogue: sidebar
 * filters (destinations, country, safari type, activities, length and
 * budget sliders), search, sort and pagination over all 61 safaris.
 * Flows with the page, so put any content above and below the shortcode.
 */
function kambu_safaris_browse_shortcode() {
	$file = plugin_dir_path( __FILE__ ) . 'fragment-browse.html';
	if ( ! is_readable( $file ) ) {
		return '<p>The Kambu safari finder is missing its fragment-browse.html file. Reinstall the plugin, or book via WhatsApp +254 769 103 670.</p>';
	}
	return file_get_contents( $file );
}
add_shortcode( 'kambu_safaris_browse', 'kambu_safaris_browse_shortcode' );
