<?php 
// http://php.net/manual/en/function.exec.php
// if we have POST value named "clicked"
if(isset($_POST['clicked'])){

	if($_POST['clicked']  == 'true' ){
		// executing the command : sudo python relay_on.py id
		// where the id is the number of relay that we want to switch on/off
		exec("sudo python /home/pi/relay_on.py " . $_POST['relayId']);
		echo "true";
	}else{
		exec("sudo python /home/pi/relay_off.py " . $_POST['relayId']);
		echo "false";
	}
}
