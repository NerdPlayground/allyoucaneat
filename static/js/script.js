function EditDetail(element_id){
    document.getElementById(element_id).disabled = false;
}

function SaveDetail(element_id){
    document.getElementById(element_id).disabled = false;
}

function AddContent(element_id){
    content_section= document.createElement("div");
    content_section.id= "content-section";

    content= document.createElement("input");
    content.id= "content-input";
    content.setAttribute("name","content-input");
    content.setAttribute("type","text");
    content.setAttribute("placeholder","Enter Content");
    content.setAttribute("required",true);

    remove_content= document.createElement("button");
    remove_content.id= "remove-content-button";
    remove_content.innerText= "Remove";
    remove_content.setAttribute("type","button");
    remove_content.setAttribute(
        "onclick",
        "RemoveContent(remove_content.id)"
    );

    content_section.appendChild(content);
    content_section.appendChild(remove_content);

    section= document.getElementById(element_id);
    section.appendChild(content_section);
}

function AddPrice(element_id){
    price_section= document.createElement("div");
    price_section.id= "price-section";
    
    price_type= document.createElement("input");
    price_type.id= "price-type-input";
    price_type.setAttribute("name","price-type-input");
    price_type.setAttribute("type","text");
    price_type.setAttribute("placeholder","Enter Type");
    price_type.setAttribute("required",true);
    
    label_price_type= document.createElement("label")
    label_price_type.setAttribute("for",price_type.id);
    label_price_type.innerText= "Type: "
    
    price= document.createElement("input");
    price.id= "price-input";
    price.setAttribute("name","price-input");
    price.setAttribute("type","number");
    price.setAttribute("placeholder","Enter Price");
    price.setAttribute("required",true);

    label_price= document.createElement("label")
    label_price.setAttribute("for",price.id);
    label_price.innerText= "Price: "

    remove_price= document.createElement("button");
    remove_price.id= "remove-price-button";
    remove_price.innerText= "Remove";
    remove_price.setAttribute("type","button");
    remove_price.setAttribute(
        "onclick",
        "RemoveContent(remove_price.id)"
    );

    price_section.appendChild(label_price_type);
    price_section.appendChild(price_type);
    price_section.appendChild(label_price);
    price_section.appendChild(price);
    price_section.appendChild(remove_price);

    section= document.getElementById(element_id);
    section.appendChild(price_section);
}

function RemoveContent(element_id){
    document.getElementById(element_id).parentNode.remove();
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