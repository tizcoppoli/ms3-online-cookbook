$(document).ready(function () {    

    $(".sidenav").sidenav({ edge: "right" });
    $(".collapsible").collapsible();
    $(".tooltipped").tooltip();
    $("select").formSelect();
    $('.parallax').parallax();
    $('.materialboxed').materialbox();
     $('.modal').modal();
    $(".dropdown-trigger").dropdown({ hover: false });
    $('.carousel.carousel-slider').carousel({
        fullWidth: true,
        indicators: true
    }, setTimeout(autoplay, 4000));

    $(".datepicker").datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });

    validateMaterializeSelect();
    setInterval(changeLinkToButton, 500);

    

});

function autoplay() {
    $('.carousel').carousel('next');
    setTimeout(autoplay, 4000);
}

function changeLinkToButton() {
    href = $(".carousel-item.active").attr("href");
    $("#carousel-button").attr("href", href)
}

function validateMaterializeSelect() {
    let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
    let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
    if ($("select.validate").prop("required")) {
        $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
    }
    $(".select-wrapper input.select-dropdown").on("focusin", function () {
        $(this).parent(".select-wrapper").on("change", function () {
            if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                $(this).children("input").css(classValid);
            }
        });
    }).on("click", function () {
        if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
            $(this).parent(".select-wrapper").children("input").css(classValid);
        } else {
            $(".select-wrapper input.select-dropdown").on("focusout", function () {
                if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                    if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                        $(this).parent(".select-wrapper").children("input").css(classInvalid);
                    }
                }
            });
        }
    });
}

$("#add_recipe").on("click", function() {

    new_ingredient_input = 
    `<div class="input-field col s12">
        <div class="col s10 no-padding">
            <input type="text" name="ingredient_list[]" minlength="5"
                    maxlength="2000" class="validate" 
                    required placeholder="New Ingredient">            
        </div>
        <div class="col s2">
            <button type="button" class="delete_ingredient_button btn"><i class="fas fa-trash"></i></button>
        </div>
    </div>`;
    
    $("#ingredients_wrapper").append(new_ingredient_input);
    $(".delete_ingredient_button").on("click", function() {
       $(this).parent().parent().remove();
    });
} );

$(".delete_ingredient_button").on("click", function() {
    $(this).parent().parent().remove();
});

$("#add_recipe_step").on("click", function() {

    new_step_input = 
    `<div class="input-field col s12">
        <div class="col s10 no-padding">
            <input type="text" name="recipe_steps[]" minlength="5"
                    maxlength="2000" class="materialize-textarea validate" 
                    required placeholder="New Step">            
        </div>
        <div class="col s2">
            <button type="button" class="delete_step_button btn"><i class="fas fa-trash"></i></button>
        </div>
    </div>`;
    
    $("#steps_wrapper").append(new_step_input);
    $(".delete_step_button").on("click", function() {
       $(this).parent().parent().remove();
    });
} );

$(".delete_step_button").on("click", function() {
    $(this).parent().parent().remove();
 });


