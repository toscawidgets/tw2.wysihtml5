<%namespace name="tw" module="tw2.core.mako_util"/>

  <div id="${w.toolbar_id}" style="display: none;">
    <div class="btn-group">
      <a class="btn btn-small" data-wysihtml5-command="bold" title="bold [CTRL+B]"><i class="icon-bold"></i>&nbsp;</a>
      <a class="btn btn-small" data-wysihtml5-command="italic" title="italic [CTRL+I]"><i class="icon-italic"></i>&nbsp;</a>
      <a class="btn btn-small" data-wysihtml5-command="createLink" title="Insert link"><i class="icon-share-alt"></i>&nbsp;</a>
      <a class="btn btn-small" data-wysihtml5-command="insertImage" title="Insert picture"><i class="icon-picture"></i>&nbsp;</a>
      <a class="btn btn-small" data-wysihtml5-command="formatBlock" data-wysihtml5-command-value="h1">h1</a>
      <a class="btn btn-small" data-wysihtml5-command="formatBlock" data-wysihtml5-command-value="h2">h2</a>
      <a class="btn btn-small" data-wysihtml5-command="insertUnorderedList" title="Unordered list"><i class="icon-list"></i>&nbsp;ul</a>
      <a class="btn btn-small" data-wysihtml5-command="insertOrderedList" title="Ordered list"><i class="icon-list"></i>&nbsp;ol</a>
      <a class="btn btn-small" data-wysihtml5-command="foreColor" data-wysihtml5-command-value="red" style="color: red;">red</a>
      <a class="btn btn-small" data-wysihtml5-command="foreColor" data-wysihtml5-command-value="green" style="color: green;">green</a>
      <a class="btn btn-small" data-wysihtml5-command="foreColor" data-wysihtml5-command-value="blue" style="color: blue;">blue</a>
      <a class="btn btn-small" data-wysihtml5-action="change_view" title="switch to html view"><i class="icon-chevron-left"></i>&nbsp;<i class="icon-chevron-right"></i></a>
    </div>
    
    <div data-wysihtml5-dialog="createLink" style="display: none;" class="form-inline">
      <label>
        Link:
        <input data-wysihtml5-dialog-field="href" value="http://" class="input-medium">
      </label>
      <a data-wysihtml5-dialog-action="save" class="btn btn-mini btn-primary">OK</a>
      <a data-wysihtml5-dialog-action="cancel" class="btn btn-mini">Cancel</a>
    </div>
    
    <div data-wysihtml5-dialog="insertImage" style="display: none;" class="form-inline">
      <label>
        Image:
        <input data-wysihtml5-dialog-field="src" value="http://" class="input-medium">
      </label>
      <label>
        Align:
        <select data-wysihtml5-dialog-field="className" class="input-small">
          <option value="">default</option>
          <option value="wysiwyg-float-left">left</option>
          <option value="wysiwyg-float-right">right</option>
        </select>
      </label>
      <a data-wysihtml5-dialog-action="save" class="btn btn-mini btn-primary">OK</a>
      <a data-wysihtml5-dialog-action="cancel" class="btn btn-mini">Cancel</a>
    </div>
    
  </div>

<textarea ${tw.attrs(attrs=w.attrs)}>${w.value or ''}</textarea>
