<!-- modal options for crawler -->
<div class="modal fade" id="modal-options">
	<div class="modal-dialog">
		<div class="modal-content">
			<div class="modal-header">
				<!-- <button class="close" data-dismis="modal" class="close">&times;</button> -->
				<h3>Các tùy chọn cho Crawler</h3>
			</div>
			<div class="modal-body">
				<form action="" method="post">
					<div class="row">
						<div class="col-md-6">
							<label><input type="checkbox" value="1" name="opt[opt1]">&nbsp;Not js, css</label><br>
							<label><input type="checkbox" value="1" name="opt[opt3]" onchange="addLimitAmount();" id="amount-checkbox">&nbsp;Limit amounts</label >
							<label><div id="amount-input" class="col-md-6"></div></label >
<script type="text/javascript">
	function addLimitAmount(){
			var amount_checkbox = document.getElementById("amount-checkbox");
			var amount_input = document.getElementById("amount-input");
			var input = "<input class='form-control' type='text'>";
			if (amount_checkbox.checked){
				amount_input.innerHTML = input;
			}else{
				amount_input.innerHTML = "";
			}

	}

</script>
						</div>
						<div class="col-md-6">
							<label><input type="checkbox" name="opt[opt2]">&nbsp;ALL</label><br>
							<label><input type="checkbox" value="1" name="opt[opt4]">&nbsp;Only php, jsp, aspx, ...</label><br>
							<label>
						</div>
					</div><!-- end row -->
				</form>
			</div><!-- end modal-body -->
			<div class="modal-footer">
				<button class="btn btn-default" onclick="setOptionSelect();" data-dismiss="modal">OK</button>
				<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
			</div><!-- end modal-footer -->
		</div><!-- end modal-content -->
	</div><!-- end modal dialog -->
</div><!-- end #modal-options -->