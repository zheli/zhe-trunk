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

require_once (JPATH_SITE.DS.'components'.DS.'com_content'.DS.'helpers'.DS.'route.php');

class modBowSlideshowHelper
{
	function getList(&$params)
	{
		global $mainframe;

		$source		= $params->get('source', '');
		$path 	= JPATH_SITE ."/".$source;
		$images 	= JFolder::files( $path );
		$lists = array();
		$i = 0;
		foreach ($images as $image){
			$temp 	= $path .'/'. $image;
			if ( @eregi( "bmp|gif|jpg|png|jpeg", $image ) && is_file( $temp ) ) {
				$lists[$i] = JURI::base().$source."/".$image;
				$i++;
			}
		}
		
		return $lists;
	}
	function getArticleContent($id){
			
		$db			=& JFactory::getDBO();
		
		$query = 'SELECT a.* ' .
		' FROM #__content AS a' .
		' WHERE a.id=' .$id;
		$db->setQuery($query);
		$rows = $db->loadObjectList();
		$row = $rows[0];
		$row->introtext = modBowSlideshowHelper::cleanHtml($row->introtext);	
		return $row;
	}
	function truncString($str = "", $len = 150, $more = 'true') {
			if ($str == "") return $str;
			if (is_array($str)) return $str;
			$str = trim($str);
			// if it's les than the size given, then return it
			if (strlen($str) <= $len) return $str;
			// else get that size of text
			$str = substr($str, 0, $len);
			// backtrack to the end of a word
			if ($str != "") {
			  // check to see if there are any spaces left
			  if (!substr_count($str , " ")) {
				if ($more == 'true') $str .= "...";
				return $str;
			  }
			  // backtrack
			  while(strlen($str) && ($str[strlen($str)-1] != " ")) {
				$str = substr($str, 0, -1);
			  }
			  $str = substr($str, 0, -1);
			  if ($more == 'true') $str .= "...";
			  if ($more != 'true' and $more != 'false') $str .= $more;
			}
			return $str;
  }
  function cleanHtml($clean_it) {

	$clean_it = preg_replace('/\r/', ' ', $clean_it);
	$clean_it = preg_replace('/\t/', ' ', $clean_it);
	$clean_it = preg_replace('/\n/', ' ', $clean_it);

	$clean_it= nl2br($clean_it);

// update breaks with a space for text displays in all listings with descriptions
	while (strstr($clean_it, '<br>')) $clean_it = str_replace('<br>', ' ', $clean_it);
	while (strstr($clean_it, '<br />')) $clean_it = str_replace('<br />', ' ', $clean_it);
	while (strstr($clean_it, '<br/>')) $clean_it = str_replace('<br/>', ' ', $clean_it);
	while (strstr($clean_it, '<p>')) $clean_it = str_replace('<p>', ' ', $clean_it);
	while (strstr($clean_it, '</p>')) $clean_it = str_replace('</p>', ' ', $clean_it);

// temporary fix more for reviews than anything else
	while (strstr($clean_it, '<span class="smallText">')) $clean_it = str_replace('<span class="smallText">', ' ', $clean_it);
	while (strstr($clean_it, '</span>')) $clean_it = str_replace('</span>', ' ', $clean_it);

	while (strstr($clean_it, '  ')) $clean_it = str_replace('  ', ' ', $clean_it);

// remove other html code to prevent problems on display of text
	$clean_it = strip_tags($clean_it);
	return $clean_it;
  }
}
