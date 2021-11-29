<?php
	$s_name=$_POST['s_name'];
	$s_id=$_POST['s_id'];
	$s_pwd=$_POST['s_pwd'];
	if($s_id=='456' & $s_pwd=='123')
	{
		header("refresh:0; url=store01.php");
		setcookie("s_name",$s_name,time()+3600*72);
	}else
	{
		echo "<center><b>帳號或密碼錯誤";
		header("refresh:3; url=store login.php");
	}
?>