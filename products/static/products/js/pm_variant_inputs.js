// Handles add/edit product variants
var variantCount = 0;

// Add inputs for adding a vairant
$('#add-variant').on('click', function(){
    variantAmount = $('.variant').length;
    variantInputs = `
        <fieldset id="variant-${variantAmount + 1}" class="variant rounded mt-3">
            <legend class="fieldset-label font-size-1 font-weight-bold p-2 w-auto">New Variant ${variantAmount + 1}</legend>
            <label for="variant-name-${variantAmount + 1}">Variant Name*</label>
            <input type="text" id="variant-name-${variantAmount + 1}" name="variant-name-${variantAmount + 1}" class="form-input w-100 d-block" maxlength="100" required>
            <label for="variant-sku-${variantAmount + 1}" class="mt-2">Variant SKU</label>
            <input type="text" id="variant-sku-${variantAmount + 1}" name="variant-sku-${variantAmount + 1}"  class="form-input w-100 d-block" maxlength="100">
            <label for="variant-images-${variantAmount + 1}" class="mt-2 d-block">Variant Images</label>
            <div class="image-upload">
                <div class="cta cta--third d-block file-input mt-3">
                    Select Image(s) <input type="file" id="variant-images-${variantAmount + 1}" accept="image/*" name="variant-images-${variantAmount + 1}" class="images-input" multiple>
                </div>
                <p class="filename add-highlight mt-3"></p>
            </div>
            <p class="info-highlight mt-3">Only .png and .jpg files are supported</p>
            <p class="info-highlight mt-3">Default image can be set on the edit page after product is saved</p>
            <button type="button" class="variant-delete cta cta--delete d-block mt-4" value="#variant-${variantAmount + 1}">Delete</button>
        </fieldset>
    `;
    $('#add-variant').before(variantInputs);
    variantCount = variantAmount + 1;
    $('#variant-count').val(variantCount);
});

// Deletion of New Variant
$(document).on('click', '.variant-delete', function() {
    variant = $(this).val();
    variantNum = variant.split('-')[1];
    markVariant = `#variant-mark-delete-${variantNum}`;
    $(variant).remove();
    variantCount = variantAmount - 1;
    $('#variant-count').val(variantCount);

    //  Re orders variant ids
    var variants = document.getElementsByClassName('variant');

    for (i = 0; i < variants.length; ++i) {
        variant = variants[i];

        variant.setAttribute('id', `variant-${i + 1}`);

        // Legend
        legend = variant.getElementsByTagName('legend');
        legend[0].innerHTML = `Variant ${i + 1}`;

        input = variant.getElementsByTagName('input');
        label = variant.getElementsByTagName('label');
        button = variant.getElementsByTagName('button');

        // Name
        label[0].setAttribute('for', `variant-name-${i + 1}`);
        input[0].setAttribute('id', `variant-name-${i + 1}`);
        input[0].setAttribute('name', `variant-name-${i + 1}`);
        
        // SKU
        label[1].setAttribute('for', `variant-sku-${i + 1}`);
        input[1].setAttribute('id', `variant-sku-${i + 1}`);
        input[1].setAttribute('name', `variant-sku-${i + 1}`);
        
        // Images
        label[2].setAttribute('for', `variant-images-${i + 1}`);
        input[2].setAttribute('id', `variant-images-${i + 1}`);
        input[2].setAttribute('name', `variant-images-${i + 1}`);

        // Button
        button[0].setAttribute('value', `#variant-${i + 1}`);
    }
});

// Toggle indicator to show which image will be set to default on edit page
$('.image-selector').on('change', function() {
    $('.image-selector').parent().find('label').removeClass('default');
    $('.image-selector:radio:checked').next('label').addClass('default');
});

$('.variant-image-selector').on('change', function() {
    $('.variant-image-selector').parent().find('label').removeClass('default');
    $('.variant-image-selector:radio:checked').next('label').addClass('default');
});

// Show selected product image filename
$(document).on('change','.images-input', function() {
    var id = $(this).attr('id');
    var input = document.getElementById(id); // JQuery didnt work
    $(this).parent().parent().find('p').text('');
    for (var i = 0; i < input.files.length; ++i) {
        var name = input.files.item(i).name;
        if (i == 0) {
            $(this).parent().parent().find('p').append(`Images to be uploaded on save:<br>${name}`);
        }

        else {
            $(this).parent().parent().find('p').append(`,<br>${name}`);
        }
    }
});
