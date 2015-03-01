<html>
  <head>
    <?php 
       $command_output = [];
       if (isset($_POST['LampON']))
       {
       exec('python ../SmartPlug/lampControl.py on',$command_output);
       }
       if (isset($_POST['LampOFF']))
       {
       exec('python ../SmartPlug/lampControl.py off',$command_output);
       }
       ?>

    <title></title>
  </head>
  <body>
    <form method="post">
      <table
	  <tr>
            <td style="text-align: center;">Turn lamp on</td>
            <td style="text-align: center;">Turn lamp off</td>
	  </tr>
	  <tr>
	    <td style="text-align: center;"><button name="LampON">Lamp On</button></td>
	    <td style="text-align: center;"><button name="LampOFF">Lamp Off</button></td>
	  </tr>
      </table>
    </form>
    <p><?php
		foreach ($command_output as $line) {
			echo $line;
			echo "<br>";
		}	
	?>
    </p>
  </body>
</html>
