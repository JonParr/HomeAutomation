<html>
  <head>
    <?php 
       if (isset($_POST['LampON']))
       {
       exec('python ../SmartPlug/lampControl.py on');
       }
       if (isset($_POST['LampOFF']))
       {
       exec('python ../SmartPlug/lampControl.py off');
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
  </body>
</html>
