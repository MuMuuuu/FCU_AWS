<!DOCTYPE html>
<head>
	<title>
		Cloud Application Team 5
	</title>
	<link  href="user_information.css" type="text/css" rel="stylesheet" >
	<meta name="viewport" content="width=device-width , initial-scale=1.0" />
</head>
	
<body>
		
	<p><button class="refresh" onclick="window.location.reload();" >refresh</button>
		<button class="logout" onclick="location.href='login.php'" >logout</button></p>
	<?php
		$name=$_COOKIE['name'];
		echo "<p><b><font size=10px>".$name."</b></p>";
	?>
	<table  class="table1">
			<td rowspan=2><center><img src="virus.png" width=100px height=100px ></td>
			<td><font size=1><b>Covid-19 risk status</b></td>
		<tr><td><b><font size=5>低風險*</b></td>
	</table>
	
	<p><table class="table2">
			<th rowspan=4><iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4178.025498841629!2d120.64382907548395!3d24.17475474069062!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x346916217034b333%3A0x35dce5a0e32c09b0!2z5YWo5a625L6_5Yip5ZWG5bqXIOWPsOS4remHkeemj-aYn-W6lw!5e0!3m2!1szh-TW!2stw!4v1637470410087!5m2!1szh-TW!2stw" width=100px height=100px style="border:0;" allowfullscreen="" loading="lazy"></iframe></th>
			<th></th><th><font size=1>history</th>
		<tr><td><b><font size=2>Last Check-in</b></td><th rowspan=3><input type=submit name="check" value="check*"></th>
		<tr><td><b><font size=5px>福星全家*</b></th>
		<tr><td><b><font size=1>Date,Time</b></td>
	</table></p>
	
	<table class="table3">
		<th><font size=20>QR碼</th>
		<tr><th><font size=20>掃描</th>
	</table>
	
</body>
