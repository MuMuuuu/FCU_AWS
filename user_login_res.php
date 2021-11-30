<?php
	$name=$_POST['name'];
	$id=$_POST['id'];
	$pwd=$_POST['pwd'];
	if($id=='123' & $pwd=='456')
	{
		header("refresh:0; url=user_information.php");
		setcookie("name",$name,time()+3600*72);
	}else
	{
		echo "<center><b>帳號或密碼錯誤";
		header("refresh:3; url=user_login.php");
	}
?>
