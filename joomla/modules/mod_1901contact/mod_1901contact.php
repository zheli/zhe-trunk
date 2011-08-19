<?php
  /**
 *1901 Contact form module
 @package 1901 Contact form for Joomla! 1.5
 * @link       http://www.a.1901webdesign.com/
* @copyright (C) 2011- Nikolaos Koliopoulos
 * @license GNU/GPL http://www.gnu.org/copyleft/gpl.html
 */
defined('_JEXEC') or die('Restricted access');

JHTML::_('behavior.calendar');

JHTMLBehavior::formvalidation();


require_once (dirname(__FILE__).DS.'helper.php');


$loDoc =& JFactory::getDocument();
$loDoc->addScript(JURI::root().'modules/mod_1901contact/mod_1901contact.js');
$loDoc->addStyleSheet(JURI::root().'modules/mod_1901contact/mod_1901contact.css');


$lsSubmitText = $params->get('submit_button', 'Contact');
$lsStyleSuffix = $params->get('moduleclass_sfx', null);

$lsAction = JRequest::getVar('1901contactAction', null, 'POST');
if ($lsAction == 'send') {
    $lsMessage = mod1901contactHelper::sendEmail($params);
}


if (!isset($lsMessage)) $lsMessage = $params->get('introtext');

$credit = @$params->get( 'credit');
?>
<script language="javascript">
	function my1901contactValidate(f)
	{
		if (document.formvalidator.isValid(f)) {
			f.check.value='<?php echo JUtility::getToken(); ?>'; 
			return true; 
		} else {
			alert('Some values are not acceptable. Please retry.');
		}
		return false;
	}
</script>
<div id="formContact"><?php echo $lsStyleSuffix; ?>
	<?php if($lsMessage != ""){ ?>
	<p><?php echo $lsMessage; ?></p>
	<?php } ?>
	<form id="contactForm" method="post" class="form-validate" onSubmit="return my1901contactValidate(this);" action="<?php echo $_SERVER['REQUEST_URI']; ?>">
		<div class="cformlabel">Name</div><div class="cforminput"><input type="text" name="name" value="" onFocus="clear1901contactText(this)" class="inputbox" /></div>
		<div class="cformlabel">Email</div><div class="cforminput"><input type="text" name="email" value="" onFocus="clear1901contactText(this)" class="inputbox required validate-email" /></div>
		<div class="cformlabel">Phone</div><div class="cforminput"><input type="text" name="Phone" value="" onFocus="clear1901contactText(this)" class="inputbox" /></div>
		<div class="cformlabel">Nr. of Beds</div><div class="cforminput" style="width:50px;"><input type="text" name="bed" value="" onFocus="clear1901contactText(this)" class="inputbox" style="width:50px;"/></div><div class="cformlabel" style="width:80px;margin-left:15px;">Nr. of Guests</div><div class="cforminput" style="width:50px;"><input type="text" name="guest" value="" onFocus="clear1901contactText(this)" class="inputbox" style="width:50px;"/></div>
		<div class="cformlabel">Check in</div><div class="cforminput"><?php echo JHTML::calendar('','checkin', 'checkin',"%d-%m-%Y"); ?></div>
		<div class="cformlabel">Check out</div><div class="cforminput"><?php echo JHTML::calendar('','checkout', 'checkout',"%d-%m-%Y"); ?></div>
		<div class="clear"></div>
		<input type="submit" value="<?php echo $lsSubmitText; ?>" class="button" />
		<input type="hidden" name="1901contactAction" value="send" />
		<input type="hidden" name="check" value="post" />
	</form>
</div>