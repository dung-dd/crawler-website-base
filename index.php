<!DOCTYPE html>
<html>
<head>
	<title>Crawler</title>
	<meta charset="utf-8">
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<link rel="stylesheet" href="css/bootstrap-theme.min.css">
	<link rel="stylesheet" href="css/styles.css">
	<script src="js/jquery-1.12.0.min.js"></script>
	<script src="js/bootstrap.min.js"></script>
	<script src="js/handle.js"></script>

<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js"></script>
<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>


</head>
<body>
<!-- ------------------------ header ---------------------- -->
<div id="header">
<?php 
	include "modules/navbar.php";
?>
</div><!-- end header -->


<!-- ------------------------ body ---------------------- -->
<div id="body">
	<div id="submit">
		<form action="" method="post">
			<center>	
				<input type="text" class="input-lg" placeholder="Nhập URL hoặc IP, exam: domain.com:port/module" name="url">
				<br><br>
				<button type="submit" class="btn-primary btn-lg btn-search " name="search">
					<span class="glyphicon glyphicon-search">&nbsp;Crawler</span> 
				</button>
			</center>
		</form>

	<!-- ---------------- module results ---------------- -->
	<?php 	include "modules/results.php"; ?> 


</div><!-- end body -->

<!-- -------------------------- footer -------------------------- -->
<div id="footer">
	<p id="footer-center" class="footer">
		Copy right &copy; 2016
	</p>
</div><!-- end footer -->



</body>
</html>
