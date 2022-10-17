let content_button_clicked_counter= 0;
function AddContent(element_id){
    ++content_button_clicked_counter;
    const parent_container= document.getElementById(element_id);

    const content_container= document.createElement("div");
    content_container.id= "new-product-content-"+content_button_clicked_counter;
    content_container.className= "new-product-content";

    const content_container_fields= document.createElement("div");
    content_container_fields.id= "new-product-content-fields-"+content_button_clicked_counter;
    content_container_fields.className= "new-product-content-fields";

    const content_value_container= document.createElement("div");
    content_value_container.className= "form-group";

    const content_value= document.createElement("input");
    content_value.id= "new-product-content-value-"+content_button_clicked_counter;
    content_value.setAttribute("name","new-product-content-value");
    content_value.setAttribute("type","text");
    content_value.setAttribute("placeholder","Enter Content");
    content_value.setAttribute("required",true);

    content_value_container.appendChild(content_value);
    content_container_fields.appendChild(content_value_container);

    const content_container_buttons= document.createElement("div");
    content_container_buttons.id= "new-product-content-buttons-"+content_button_clicked_counter;
    content_container_buttons.className= "new-product-content-buttons";

    const remove_content= document.createElement("button");
    remove_content.id= "remove-content-button-"+content_button_clicked_counter;
    remove_content.classList.add("remove-content-button","all-buttons");
    remove_content.innerText= "Remove";
    remove_content.setAttribute("type","button");
    remove_content.setAttribute(
        "onclick",
        "RemoveContainer(this.id)"
    );
    content_container_buttons.appendChild(remove_content);

    content_container.appendChild(content_container_fields);
    content_container.appendChild(content_container_buttons);
    parent_container.appendChild(content_container);
}

let price_button_clicked_counter= 0;
function AddPrice(element_id){
    ++price_button_clicked_counter;
    const parent_container= document.getElementById(element_id);
    
    const price_container= document.createElement("div");
    price_container.id= "new-product-price-"+price_button_clicked_counter;
    price_container.className= "new-product-price";

    const price_container_fields= document.createElement("div");
    price_container_fields.id= "new-product-price-fields-"+price_button_clicked_counter;
    price_container_fields.className= "new-product-price-fields";

    const price_type_container= document.createElement("div");
    price_type_container.className= "form-group";

    const price_type= document.createElement("input");
    price_type.id= "new-product-price-type-"+price_button_clicked_counter;
    price_type.className= "new-product-price-type";
    price_type.setAttribute("name","new-product-price-type");
    price_type.setAttribute("type","text");
    price_type.setAttribute("placeholder","Enter Type");
    price_type.setAttribute("required",true);
    
    const label_price_type= document.createElement("label");
    label_price_type.setAttribute("for",price_type.id);
    label_price_type.innerText= "Type: ";

    price_type_container.appendChild(label_price_type);
    const tnewline= document.createElement("br");
    price_type_container.appendChild(tnewline);
    price_type_container.appendChild(price_type);

    const price_value_container= document.createElement("div");
    price_value_container.className= "form-group";

    const price_value= document.createElement("input");
    price_value.id= "new-product-price-value-"+price_button_clicked_counter;
    price_value.className= "new-product-price-value";
    price_value.setAttribute("name","new-product-price-value");
    price_value.setAttribute("type","text");
    price_value.setAttribute("placeholder","Enter Value");
    price_value.setAttribute("required",true);
    
    const label_price_value= document.createElement("label");
    label_price_value.setAttribute("for",price_value.id);
    label_price_value.innerText= "Price: ";

    price_value_container.appendChild(label_price_value);
    const pnewline= document.createElement("br");
    price_value_container.appendChild(pnewline);
    price_value_container.appendChild(price_value);

    price_container_fields.appendChild(price_type_container);
    price_container_fields.appendChild(price_value_container);

    const price_container_buttons= document.createElement("div");
    price_container_buttons.id= "new-product-price-buttons-"+price_button_clicked_counter;
    price_container_buttons.className= "new-product-price-buttons";

    const remove_price= document.createElement("button");
    remove_price.id= "remove-price-button-"+price_button_clicked_counter;
    remove_price.classList.add("remove-price-button","all-buttons");
    remove_price.innerText= "Remove";
    remove_price.setAttribute("type","button");
    remove_price.setAttribute(
        "onclick",
        "RemoveContainer(this.id)"
    );
    price_container_buttons.appendChild(remove_price);

    price_container.appendChild(price_container_fields);
    price_container.appendChild(price_container_buttons);
    parent_container.appendChild(price_container);
}

function RemoveContainer(element_id){
    const grandparent= document.getElementById(element_id).parentNode.parentNode;
    grandparent.remove();
}

function RestrictOptions(form_id,elements_name){
    boxes= document.forms[form_id].elements[elements_name];
    let counter= 0;
    for(let c=0; c<boxes.length; ++c)
        if(boxes[c].checked) ++counter;

    if(counter == 4){
        for(let c=0; c<boxes.length; ++c)
            if(!boxes[c].checked)
                boxes[c].disabled= true;
    }
    else{
        for(let c=0; c<boxes.length; ++c)
            if(!boxes[c].checked)
                boxes[c].disabled= false;
    }
}

function RemoveOption(element_id,form_id,elements_name){
	let counter= 0;
    boxes= document.forms[form_id].elements[elements_name];
	for(let c=0; c<boxes.length; ++c)
		if(boxes[c].checked == false) ++counter;
	if(counter > 1)
		document.getElementById(element_id).checked= true;
}

function ViewPortValues(){
    let output= "";
    let container= document.getElementById("main-container");
    output += "Viewport Width: " +window.innerWidth +"\n";
    output += "Viewport Height: " +window.innerHeight +"\n";
    output += "Main Width: " +container.offsetWidth +"\n";
    output += "Main Height: " +container.offsetHeight +"\n";
    alert(output);
}