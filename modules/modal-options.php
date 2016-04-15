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
							<label><input type="checkbox" value="1" name="opt[opt1]">&nbsp;Option</label><br>
							<label><input type="checkbox" value="1" name="opt[opt2]">&nbsp;Option</label><br>
							<label><input type="checkbox" value="1" name="opt[opt3]">&nbsp;Option</label>
						</div>
						<div class="col-md-6">
							<label><input type="checkbox" name="opt[opt3]">&nbsp;Option</label><br>
							<label><input type="checkbox" name="opt[opt3]">&nbsp;Option</label><br>
							<label><input type="checkbox" name="opt[opt3]">&nbsp;Option</label>
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