<!DOCTYPE html>
<head>
	<title>
		Cloud Application Team 5
	</title>
	<link  href="store02.css" type="text/css" rel="stylesheet" >
	<meta name="viewport" content="width=device-width , initial-scale=1.0" />
</head>
	
<body>
    <p><button class="button" onclick="location.href='store01.php'" >顧客風險</button></p>
    <p><button class="logout" onclick="location.href='login.php'" >logout</button></p>
	<?php
		$s_name=$_COOKIE['s_name'];
		echo "<b><font size=10px>" . $s_name . "</b><br>" ;
	?>
	<br>
	<table style="font-size:8" class="table" >
		<th>QR</th>
		<tr><th>code</th> 
	</table>	
</body>
