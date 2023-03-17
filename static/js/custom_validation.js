function removevalidation() {
  document.getElementById("title").innerHTML = "";
  document.getElementById("nauthor").innerHTML = "";
  document.getElementById("ndate").innerHTML = "";
  document.getElementById("nslug").innerHTML = "";
  document.getElementById("nimage").innerHTML = "";
  document.getElementById("ndesc").innerHTML = "";
}

function validateform() {
  var ttitle = document.myform.news_title.value;
  var nauthor = document.myform.news_author.value;
  var ndate = document.myform.news_date.value;
  var nslug = document.myform.slug.value;
  var nimage = document.myform.news_img.value;
  var ndesc = document.myform.news_description.value;

  if (ttitle == null || ttitle == "") {
    document.getElementById("title").innerHTML = "Title can't be blank";
    //   document.getElementById('subbtn').disabled = true;
    return false;
  } else if (nauthor == null || nauthor == "") {
    document.getElementById("nauthor").innerText = "required";
    return false;
  } else if (ndate == null || ndate == "") {
    document.getElementById("ndate").innerText = "required ";
    return false;
  } else if (nslug == null || nslug == "") {
    document.getElementById("nslug").innerText = "required";
    return false;
  } else if (nimage == null || nimage == "") {
    document.getElementById("nimage").innerText = "required";
    return false;
  } else if (ndesc == null || ndesc == "") {
    document.getElementById("ndesc").innerText = "required";
    return false;
  }
  return true;
}



function removeEventValidation(){
  document.getElementById("etitle").innerHTML = "";
  document.getElementById("edate").innerText = "";
  document.getElementById("eslug").innerText = "";
  document.getElementById("eimg").innerText = "";
  document.getElementById("edesc").innerText = "";

}

function eventFormValidation() {
  var etitle = document.eventform.event_title.value;
  var edate = document.eventform.event_date.value;
  var eslug = document.eventform.slug.value;
  var eimg = document.eventform.event_img.value;
  var edesc = document.eventform.event_description.value;
  

  if (etitle == null || etitle == "") {
    document.getElementById("etitle").innerHTML = "Fill in the fields";
    return false;
  }
  else if (edate == null || edate == "") {
    document.getElementById("edate").innerText = "required ";
    return false;
  } else if (eslug == null || eslug == "") {
    document.getElementById("eslug").innerText = "required";
    return false;
  } 
  else if (eimg == null || eimg == "") {
    document.getElementById("eimg").innerText = "required";
    return false;
  } else if (edesc == null || edesc == "") {
    document.getElementById("edesc").innerText = "required";
    return false;
  }
  return true;
}





function removeAboutValidation(){
  document.getElementById("atitle").innerHTML = "*";
  document.getElementById("adesc").innerText = "*";
  document.getElementById("aimg").innerText = "*";
  document.getElementById("astatus").innerText = "*";

}

function aboutFormValidation() {
  var atitle = document.aboutform.about_title.value;
  var adesc = document.aboutform.about_description.value;
  var aimg = document.aboutform.about_img.value;
  var astatus = document.aboutform.status.value;
  

  if (atitle == null || atitle == "") {
    document.getElementById("atitle").innerHTML = "Fill in the fields";
    return false;
  }
  else if (adesc == null || adesc == "") {
    document.getElementById("adesc").innerText = "required ";
    return false;
  } else if (aimg == null || aimg == "") {
    document.getElementById("aimg").innerText = "required";
    return false;
  } 
  else if (astatus == null || astatus == "") {
    document.getElementById("astatus").innerText = "required";
    return false;
  } 

}
