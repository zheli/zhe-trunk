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

$document = JFactory::getDocument();

?>
<script src="<?php echo JURI::base(); ?>modules/mod_bowslideshow/tmpl/js/sliderman.1.3.0.js"></script>
<?php
	$document->addStyleSheet(JURI::base()."modules/mod_bowslideshow/tmpl/css/bowslideshow.css");
	$css= "#bowslieshow-".$module->id."{
		width: ".$width."px;
		height: ".$height."px;
	}
	"."#bowslieshow-navigation-".$module->id."{
		width: ".$width."px;
	}"
	.".bowslieshow-prev{height: ".$height."px;}"
	.".bowslieshow-next{height: ".$height."px;}"
	;
	$document->addStyleDeclaration($css);
	
?>
<div id="bowslieshow-<?php echo $module->id;?>" class="bowslieshow-container">
	<?php
	for($i=0;$i<count($list);$i++){
		$item = $list[$i];
	?>
		<?php if($links[$i] != "") echo "<a href='".$links[$i]."' />"; ?><img src="<?php echo $item; ?>" alt="" style="display:none"/><?php if($links[$i] != "") echo "</a>"; ?>
		<?php if($titles[$i] != "" || $descriptions[$i] != ""){ ?>
		<div class="bowslieshow-description" style="display:none;">
			<?php if($titles[$i] != "") echo "<strong>".$titles[$i]."</strong>:"; ?>
			<?php 
				if($descriptions[$i] != "") {
					echo $descriptions[$i];
					if($show_readmore && $links[$i] != "") echo "... <a href='".$links[$i]."' class='readmorelink' />".$readmore_text."</a>";
				}
				
			?>
		</div>
		<?php } ?>
	<?php
	}
	?>
</div>
<?php if($navigation){ ?>
<div id="bowslieshow-navigation-<?php echo $module->id;?>" class="bowslieshow-navigation"></div>
<?php } ?>
<script type="text/javascript">
window.addEvent('load', function() {
	/* predefined effects */
	Sliderman.effect({name: 'fade', fade: true, duration: 600});
	Sliderman.effect({name: 'move_left', left: true, move: true, duration: <?php echo $duration; ?>});
	Sliderman.effect({name: 'move_top', top: true, move: true, duration: <?php echo $duration; ?>});
	Sliderman.effect({name: 'move_right', right: true, move: true, duration: <?php echo $duration; ?>});
	Sliderman.effect({name: 'move_bottom', bottom: true, move: true, duration: <?php echo $duration; ?>});
	Sliderman.effect({name: 'stairs', cols: 7, rows: 5, delay: 30, order: 'straight_stairs', road: 'BL', fade: true});
	Sliderman.effect({name: 'blinds', cols: 10, delay: 100, duration: <?php echo $duration; ?>, order: 'straight', right: true, zoom: true, fade: true});
	Sliderman.effect({name: 'rain', cols: 10, delay: 100, duration: <?php echo $duration; ?>, order: 'straight', top: true, fade: true});
	Sliderman.effect({name: 'boom', rows: 3, cols: 9, delay: 50, duration: <?php echo $duration; ?>, order: 'random', fade: true});

	bowslieshow_effects_<?php echo $module->id;?> = '<?php echo $effects; ?>';
	var bowslieshow_<?php echo $module->id;?> = Sliderman.slider({container: 'bowslieshow-<?php echo $module->id;?>', width: <?php echo $width; ?>, height: <?php echo $height; ?>, effects: bowslieshow_effects_<?php echo $module->id;?>,
		display: {
			<?php if($auto){ ?>
			autoplay: 3000
			<?php }else{ ?>
			autostart:false
			<?php } ?>
			<?php if($button){ ?>
			,buttons: {hide: <?php if($button==2) echo "true"; else echo "false"; ?>, opacity: 0, prev: {className: 'bowslieshow-prev', label: ''}, next: {className: 'bowslieshow-next', label: ''}},
			<?php } ?>
			<?php if($show_caption){ ?>
			description: {hide: <?php if($show_caption==2) echo "true"; else echo "false"; ?>,height: <?php echo $height_caption; ?>, position: '<?php echo $position_caption; ?>'}
			<?php } ?>
			<?php if($navigation){ ?>
			,navigation: {container: 'bowslieshow-navigation-<?php echo $module->id;?>', label: '<img src="<?php echo JURI::base()."modules/mod_bowslideshow/tmpl/images/clear.gif"; ?>" />',
			loading: {background: '#000000', opacity: 0.5, image: '<?php echo JURI::base()."modules/mod_bowslideshow/tmpl/images/loading.gif"; ?>'}
			}
			<?php } ?>
		}
	});
});
</script>
<div style="display:none;"><a href="http://vsmart-extensions.com">Vsmart Extensions</a></div>
<div style="clear:both;"></div>			