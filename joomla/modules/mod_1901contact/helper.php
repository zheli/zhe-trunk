<?php
  /**
 *1901 Contact form module
 @package 1901 Contact form for Joomla! 1.5
 * @link       http://www.a.1901webdesign.com/
* @copyright (C) 2011- Nikolaos Koliopoulos
 * @license GNU/GPL http://www.gnu.org/copyleft/gpl.html
 */
 
// no direct access
defined('_JEXEC') or die('Restricted access');

class mod1901contactHelper
{
	
	function sendEmail($params)
	{
		global $mainframe;
		
		$jAp =& JFactory::getApplication();
		
		if ($_POST['check'] != JUtility::getToken()) {
			if ($_POST['check'] == 'post') {
				$lsErrorMsg  = 'Please check all the fields of the contact form.<br />';
				$lsErrorMsg .= 'If your browser blocks javascript, then this form will never be successful. This is a security measure.';
				$jAp->enqueueMessage($lsErrorMsg,'error');
			}
			return false;
		}

		$lsEmail   = $params->get('receipt_email');
		$lsSubject = $params->get('subject');
		$lsThanks  = $params->get('thanks');
		$lsError   = $params->get('error');
		
		$lsUserName    		= JRequest::getVar('name', null, 'POST');
	    $lsUserEmail   		= JRequest::getVar('email', null, 'POST');
	    $lsUserphone    = JRequest::getVar('phone', null, 'POST');
	    
	    $bed    = JRequest::getVar('bed', null, 'POST');
	    $guest    = JRequest::getVar('guest', null, 'POST');
	    $checkin    = JRequest::getVar('checkin', null, 'POST');
	    $checkout    = JRequest::getVar('checkout', null, 'POST');

	    $lsUserText    		= JRequest::getVar('text', 'Not Given', 'POST');
	    
	    $lsFromEmail = $mainframe->getCfg('mailfrom');
	    $lsFromName  = $mainframe->getCfg('fromname');
	    $lsFrom 	 = array($lsFromEmail, $lsFromName);
	    
	    $lsBody = 'The following user has entered a message:'."\n";
	    $lsBody .= "Email: $lsUserEmail" . "\n";
	    $lsBody .= "Name: $lsUserName" . "\n";
	    $lsBody .= "phone: $lsUserphone" . "\n";
	    $lsBody .= "Number of Beds: $bed" . "\n";
	    $lsBody .= "Number of Guest: $guest" . "\n";
	    $lsBody .= "Check in: $checkin" . "\n";
	    $lsBody .= "Check out: $checkout" . "\n";

	    //$lsBody .= "Message: " . "\n";
	    //$lsBody .= $lsUserText . "\n\n";
	    $lsBody .= "---------------------------" . "\n";
	    
	    $loMailer =& JFactory::getMailer();
	    $loMailer->setSender($lsFrom);
	    $loMailer->addReplyTo($lsFrom);
	    $loMailer->addRecipient($lsEmail);
	    $loMailer->setSubject($lsSubject);
	    $loMailer->setBody($lsBody);
	    
	    if ($loMailer->Send() !== true) {
	    	return $lsError;
	    }
	    else {
	    	return $lsThanks;
	    }
	} 
} 
?>