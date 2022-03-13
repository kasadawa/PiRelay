# PiRelay   [![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=Z5J7ZSXG5XC8Q)

Web app for controlling 4 Array [Relay](https://github.com/kasadawa/PiRelay/blob/master/4_array_relay.jpg) module with Raspberry Pi .
For the project are used : 
- PHP
- Python
- HTML 
- Javascript
- Jquery
- Bootstrap 
- Bootstrap Switch 


![Interface image](https://github.com/kasadawa/PiRelay/blob/master/interface.JPG)



##Installation
Full Installation Guide can be found on [instructables](https://www.instructables.com/Raspberry-Pi-With-4-Relay-Module-for-Home-Automati/).

1) Install [Raspberry Pi OS](https://www.raspberrypi.com/software/operating-systems/).
2) Install apache serverr ```sudo apt-get install apache2 -y```
3) Install php library - ```sudo apt-get install libapache2-mod-php php```
4) Clone the repo: ```git clone https://github.com/kasadawa/PiRelay.git```
5) Place the files into the apache root dir (ex: /var/www/html ): ```sudo cp -r ~/PiRelay/var /```
6) Type your Pi IP address: ```http://YourPaspberryIp/index.html```

Wiring schema: 
![Interface image](https://github.com/kasadawa/PiRelay/blob/master/wiring.jpeg)


### Hints
- Get Rapsberry Pi IP address: ```hostname -I```
- For global network usage, apply a <b>port forwarding</b> setting from router. CAUTION! there will be a security risk (open port without any security layer, http connection)


##Documentation
So the basic idea is that we have index.html which is the main file. In it there are included some bootstrap-switch .css and .js files to make the buttons look better.
There is Jquery so that we can use ajax post request to get or send data to the php. The php itself execute a python script. The python script returns values to the php and the php send the values to the html . This is done for having a feedback from the device. So here is 
a schema of the concept:
![Schema image](https://github.com/kasadawa/PiRelay/blob/master/basic.jpg)

To load  index.html you need to type  YourPaspberryIp/index.html in your browser (example: `192.168.1.93/index.html`).

When the html laods, first we check the previous position of the relays or if we load the page for first time the relays will turn on:
  ````    
$(document).ready(function(){
$.ajax({
  method: "POST",
  url: "firstCheck.php",
  data: {}
})
.done(function( msg ) {
  msg = JSON.parse(msg);
  msg = JSON.parse(msg);
  for(var i = 0 ; i < 4; i++){
    if(msg[i] == true){
      $("#feedback"+(i+1)).html("Turned On");
    }else{
      $("#feedback"+(i+1)).html("Turned Off");
    }
    $("[name='relay"+(i+1)+"']").bootstrapSwitch('state',msg[i]);
  } 
});
});
  ````

The php file execute `firstCheck.py` and returns json output from the execution .
````
exec("sudo python /home/pi/firstCheck.py " ,$output);
echo json_encode($output); 
````  
firstCheck.py loops through all `GPIO pins` that we use and checks if they are turn on or off. The results are added to `arr[]` list and 
encoded to json :
````
print json.dumps({0:arr[0],1:arr[1],2:arr[2],3:arr[3]})
```` 
  
For the buttons we make an `onclick EventListener` , so when the button is clicked we make a ajax post request calling the `changeState.php` 
and sending the `state` and `id` of the relay , which we want to activate.The php file `exec()`  `relay_on.py` or `relay_off.py` with  relay `id`  depend on the `state` value.
````
exec("sudo python /home/pi/relay_on.py " . $_POST['relayId']);
//or
exec("sudo python /home/pi/relay_off.py " . $_POST['relayId']);
````
