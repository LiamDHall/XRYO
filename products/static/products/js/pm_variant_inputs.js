// Handles add/edit product variants
var variantCount = 0;

// Add inputs for adding a vairant
$('#add-variant').on('click', function(){
    variantAmount = $('.variant').length;
    variantInputs = `
        <fieldset id="variant-${variantAmount + 1}" class="variant rounded mt-3">
            <legend class="fieldset-label font-size-1 font-weight-bold p-2 w-auto">Variant ${variantAmount + 1}</legend>
            <label for="variant-name-${variantAmount + 1}">Variant Name*</label>
            <input type="text" id="variant-name-${variantAmount + 1}" name="variant-name-${variantAmount + 1}" class="w-100 d-block" maxlength="100" required>
            <label for="variant-sku-${variantAmount + 1}" class="mt-2">Variant SKU</label>
            <input type="text" id="variant-sku-${variantAmount + 1}" name="variant-sku-${variantAmount + 1}"  class="w-100 d-block" maxlength="100">
            <label for="variant-images-${variantAmount + 1}" class="mt-2 d-block">Variant Images</label>
            <input type="file" id="variant-images-${variantAmount + 1}" name="variant-images-${variantAmount + 1}" multiple>
            <br>
            <input type="checkbox" id="variant-mark-delete-${variantAmount + 1}" name="variant-mark-delete-${variantAmount + 1}" value="delete">
            <label for="variant-mark-delete-${variantAmount + 1}" class="highlight mt-2">Mark For Deletion</label>
            <button type="button" class="variant-delete cta cta--delete d-block" value="#variant-${variantAmount + 1}">Delete</button>
        </fieldset>
    `;
    $('#add-variant').before(variantInputs);
    variantCount = variantAmount + 1;
    $('#variant-count').val(variantCount);
})

// (Mark For) Deletion of Variant
$(document).on('click', '.variant-delete', function(){
    console.log('on delete ran')
    variant = $(this).val();
    variantNum = variant.split('-')[1]
    markVariant = `#variant-mark-delete-${variantNum}`
    $(markVariant).prop( "checked", true)
    message = `
        <div id="variant-delete-message-${variantNum}">
            <h4 class="highlight">variant ${variantNum} Is marked for deletion</h4>
            <button type="button" class="variant-undo cta cta--delete d-block" value="#variant-${variantNum}">Undo</button>
            <hr>
        </div>
    `;
    $(variant).before(message);
    $(variant).addClass('d-none')
})

// Undo marking for deletion
$(document).on('click', '.variant-undo', function(){
    variant = $(this).val();
    variantNum = variant.split('-')[1]
    markVariant = `#variant-mark-delete-${variantNum}`
    deleteMessage = `#variant-delete-message-${variantNum}`
    $(markVariant).prop( "checked", false)
    $(variant).removeClass('d-none')
    $(deleteMessage).remove()
})