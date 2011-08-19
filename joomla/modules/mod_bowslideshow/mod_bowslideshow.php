<?php
/*------------------------------------------------------------------------
# mod_bowslideshow - Bow Slideshow
# ------------------------------------------------------------------------
# author    Vsmart Extensions
# copyright Copyright (C) 2010 www.vsmart-extensions.com. All Rights Reserved.
# @license - http://www.gnu.org/licenses/gpl-2.0.html GNU/GPL
# Websites: http://www.vsmart-extensions.com
# Technical Support:  Forum - http://www.vsmart-extensions.com
-------------------------------------------------------------------------*/

// no direct access
defined('_JEXEC') or die('Restricted access');

// Include the syndicate functions only once
require_once (dirname(__FILE__).DS.'helper.php');

$source = $params->get('source', '');
$width = $params->get('width', 100);
$height = $params->get('height',60);
$effects = $params->get('effects','stairs');

if($effects=="random") $effects="rain,stairs,fade,move_left,move_right,move_top,move_bottom,blinds,boom";
$auto = intval($params->get('auto',"1"));
$navigation = intval($params->get('navigation',"1"));
$button = intval($params->get('button',"1"));
$show_caption = intval($params->get('show_caption',"1"));
$show_readmore = intval($params->get('show_readmore',"1"));

$using_article = intval($params->get('using_article',"0"));
$caption = html_entity_decode($params->get('caption',''));

$readmore_text = $params->get('readmore_text','Read more');

$duration = $params->get('duration','600');

$background_caption = $params->get('background_caption','#000000');
$opacity_caption = $params->get('opacity_caption','0.4');
$height_caption = $params->get('height_caption','100');
$position_caption = $params->get('position_caption','bottom');

$titles = array();
$links = array();
$descriptions = array();
if($using_article){
	$id = $params->get('id','');
	$articles = explode(",",$id);
	for($l=0;$l<count($articles);$l++){
		$content_id = $articles[$l];
		$links[$l] = JRoute::_(ContentHelperRoute::getArticleRoute($content_id));
		$contentArticle = modBowSlideshowHelper::getArticleContent($content_id);
		$titles[$l] = $contentArticle->title;
		$descriptions[$l] = $contentArticle->introtext;
	}
}else{
	if($caption != ""){
		preg_match_all("#\{(.*?)}#is",$caption,$captions);
		$captions = $captions[1];
		for($i=0;$i<count($captions);$i++){
			preg_match_all('#link\s*=\s*"([^"]*)"#is',$captions[$i],$link);
			$links[$i] = $link[1][0];
			preg_match_all('#caption\s*=\s*"([^"]*)"#is',$captions[$i],$title);
			$titles[$i] = $title[1][0];
			preg_match_all('#description\s*=\s*"([^"]*)"#is',$captions[$i],$description);
			$descriptions[$i] = $description[1][0];
		}
	}
}

JHTML::_('behavior.mootools');

$path 	= JPATH_SITE ."/".$source;
if(is_dir($path)){
	$list = modBowSlideshowHelper::getList($params);
	require(JModuleHelper::getLayoutPath('mod_bowslideshow'));
}else{
	echo "Folder source doesn't exsits!";
}