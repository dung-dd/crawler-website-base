<?php 
	set_time_limit(0);
	include "config.php"; 
	// include "../config.php"; # test
	// handle for input from User
	if (isset($_POST['search']))
	{
		$url = trim($_POST['url']);
		// $url = "tools.whitehat.vn";
		// khởi tạo socket
		if ($url === "")
		{	
			$danger = 	'<div class="alert alert-danger fade in">';
    		$danger .=	'<a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>';
    		$danger .=	'<strong>Cảnh báo!</strong> URL Không được để trống';
			$danger .=	'</div>';
			// echo "Khong de trong url";
			echo "$danger";
			exit();
		}
		
		$conn = socket_create(AF_INET, SOCK_STREAM, IPPROTO_IP);
		if (!$conn)
		{
			echo "Khong tao duoc socket";
			exit();
		}
		
		try
		{
			$mess = @socket_connect($conn, $server, $port);
			@socket_send($conn, $url, strlen($url), 0);
		}
		catch(Exception $e)
		{
			try{
				system('crawler/crawl.py\n');
				$mess = @socket_connect($conn, $server, $port);
				@socket_send($conn, $url, strlen($url), 0);	
			}
			catch (Exception $e)
			{		
				exit();
			}
			
		}
		$is_run = 1;
		$num_url = 1;
		$row = "<tr>
					<th></th>
					<th></th>
					<th></th>
				</tr>";
		while ($is_run) {
			$data = "";
			try
			{
				$mess = socket_recv($conn, $data, 1024, 0);	
			}
			catch (Exception $e){
				$is_run = 0;
			}
			if ($mess === 0 )
			{
				$is_run = 0;
				continue;
			}
			echo $row = "<tr>
					<th>$num_url</th>
					<th>$data</th>
					<th></th>
				</tr>";
			$num_url ++;
		}
		// echo $data;
		socket_close($conn);
	}

 ?>
