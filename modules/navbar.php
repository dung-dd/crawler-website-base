<nav class="navbar navbar-default navbar-fixed">
	<div class="container">
		<div class="navbar-header">
			<button class="navbar-toggle" data-toggle="collapse" data-target="#collapse"> 
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
				<span class="icon-bar"></span>
			</button>
			<a href="#" class="navbar-brand">CRAWLER</a>
		</div>
		<div class="navbar-collapse" id="collapse">
			<ul class="nav navbar-nav navbar-right">
				<li>
					<a class="btn-nav btn-default" data-toggle="modal" data-target="#modal-options" />Options</a>
					<?php 
						include "modules/modal-options.php";
					 ?>
				</li>
			</ul>
		</div>
	</div> <!-- end container-->
</nav>