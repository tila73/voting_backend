
//! news and news details form validaition
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


//! event and event details form validaition

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




//! about and about details form validaition

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
 


//! slider form validaition

function removesliderValidation(){
  document.getElementById("title").innerHTML = "*";
  document.getElementById("desc").innerText = "*";
  document.getElementById("img").innerText = "*";
  document.getElementById("statuss").innerText = "*";

}

function aboutSliderValidation() {
  var title = document.sliderform.slider_title.value;
  var desc = document.sliderform.slider_description.value;
  var img = document.sliderform.slider_img.value;
  var statuss = document.sliderform.status.value;
  

  if (title == null || title == "") {
    document.getElementById("title").innerHTML = "Fill in the fields";
    return false;
  }
  else if (desc == null || desc == "") {
    document.getElementById("desc").innerText = "required ";
    return false;
  } else if (img == null || img == "") {
    document.getElementById("img").innerText = "required";
    return false;
  } 
  else if (statuss == null || statuss == "") {
    document.getElementById("statuss").innerText = "required";
    return false;
  } 

}



//! counts form validaition

function removeCountValidation(){
  document.getElementById("cnumber").innerHTML = "*";
  document.getElementById("ctitle").innerText = "* ";

}

function CountFormValidation() {
  var cnumber = document.countform.count_number.value;
  var ctitle = document.countform.count_title.value;

  

  if (cnumber == null || cnumber == "") {
    document.getElementById("cnumber").innerHTML = "Fill in the fields";
    return false;
  }
  else if (ctitle == null || ctitle == "") {
    document.getElementById("ctitle").innerText = "required ";
    return false;
  } 

}
 

//! Testimonials and Testimonials details form validaition

function removetestimonialValidation(){
  document.getElementById("names").innerHTML = "";
  document.getElementById("designation").innerText = " ";
  document.getElementById("message").innerText = "";
  document.getElementById("statuss").innerText = "";

}

function testimonialValidation() {
  var names = document.tesimonialform.testmoni_name.value;
  var designation = document.tesimonialform.testmoni_designation.value;
  var message = document.tesimonialform.testmoni_message.value;
  var statuss = document.tesimonialform.status.value;
  

  if (names == null || names == "") {
    document.getElementById("names").innerHTML = "Fill in the fields";
    return false;
  }
  else if (designation == null || designation == "") {
    document.getElementById("designation").innerText = "required ";
    return false;
  } else if (message == null || message == "") {
    document.getElementById("message").innerText = "required";
    return false;
  } 
  else if (statuss == null || statuss == "") {
    document.getElementById("statuss").innerText = "required";
    return false;
  } 

}




//! Company form validaition

function removecompanyValidation(){
  document.getElementById("img").innerHTML = "";
  document.getElementById("title").innerText = " ";
  document.getElementById("desc").innerText = " ";
  document.getElementById("missions").innerText = "";
  document.getElementById("visions").innerText = "";
  document.getElementById("statuss").innerText = "";

}

function companyValidation() {
  var img = document.companyform.companyImg.value;
  var title = document.companyform.title.value;
  var desc = document.companyform.desc.value;
  var missions = document.companyform.mission.value;
  var visions = document.companyform.vision.value;
  var statuss = document.companyform.btnradio.value;
  

  if (img == null || img == "") {
    document.getElementById("img").innerHTML = "Fill in the fields";
    return false;
  }
  else if (title == null || title == "") {
    document.getElementById("title").innerText = "required ";
    return false;
  }
  else if (desc == null || desc == "") {
    document.getElementById("desc").innerText = "required ";
    return false;
  } else if (missions == null || missions == "") {
    document.getElementById("missions").innerText = "required";
    return false;
  } 
  else if (visions == null || visions == "") {
    document.getElementById("visions").innerText = "required";
    return false;
  } 
  else if (statuss == null || statuss == "") {
    document.getElementById("statuss").innerText = "required";
    return false;
  } 

}



//! Services form validaition

function removeserviceValidation(){
  document.getElementById("img").innerHTML = "";
  document.getElementById("title").innerText = " ";
  document.getElementById("desc").innerText = " ";
  document.getElementById("statuss").innerText = "";

}

function serviceValidation() {
  var img = document.serviceform.servicesImg.value;
  var title = document.serviceform.title.value;
  var desc = document.serviceform.desc.value;
  var statuss = document.serviceform.btnradio.value;
  

  if (img == null || img == "") {
    document.getElementById("img").innerHTML = "Fill in the fields";
    return false;
  }
  else if (title == null || title == "") {
    document.getElementById("title").innerText = "required ";
    return false;
  }
  else if (desc == null || desc == "") {
    document.getElementById("desc").innerText = "required ";
    return false;
  } 
  else if (statuss == null || statuss == "") {
    document.getElementById("statuss").innerText = "required";
    return false;
  } 

}




//! whychoose form validaition

function removewhyValidation(){
  document.getElementById("title").innerText = " ";
  document.getElementById("img").innerHTML = "";
  document.getElementById("desc").innerText = " ";
  document.getElementById("statuss").innerText = "";

}

function whyValidation() {
  var title = document.whyform.title.value;
  var img = document.whyform.img.value;
  var desc = document.whyform.desc.value;
  var statuss = document.whyform.btnradio.value;
  

  if (title == null || title == "") {
    document.getElementById("title").innerText = "required ";
    return false;
  }
  else if(img == null || img == "") {
    document.getElementById("img").innerHTML = "Fill in the fields";
    return false;
  }
  else if (desc == null || desc == "") {
    document.getElementById("desc").innerText = "required ";
    return false;
  } 
  else if (statuss == null || statuss == "") {
    document.getElementById("statuss").innerText = "required";
    return false;
  } 

}




//! Teams form validaition

function removeteamValidation(){
  document.getElementById("title").innerText = " ";
  document.getElementById("img").innerHTML = "";
  document.getElementById("desc").innerText = " ";
  document.getElementById("statuss").innerText = "";

}

function teamValidation() {
  var title = document.teamform.title.value;
  var desc = document.teamform.sub_desc.value;
  var img = document.teamform.img.value;
  var names = document.teamform.name.value;
  var posts = document.teamform.post.value;
  var fbl = document.teamform.fb_link.value;
  var twt = document.teamform.twitter_link.value;
  var igm = document.teamform.insta_link.value;
  

  if (title == null || title == "") {
    document.getElementById("title").innerText = "required ";
    return false;
  }
  else if(desc == null || desc == "") {
    document.getElementById("desc").innerHTML = "Fill in the fields";
    return false;
  }
  else if (img == null || img == "") {
    document.getElementById("img").innerText = "required ";
    return false;
  } 
  else if (names == null || names == "") {
    document.getElementById("names").innerText = "required";
    return false;
  } 
  else if (posts == null || posts == "") {
    document.getElementById("posts").innerText = "required";
    return false;
  } 
  else if (fbl == null || fbl == "") {
    document.getElementById("fbl").innerText = "required";
    return false;
  } 
  else if (twt == null || twt == "") {
    document.getElementById("twt").innerText = "required";
    return false;
  } 
  else if (igm == null || igm == "") {
    document.getElementById("igm").innerText = "required";
    return false;
  } 

}


//! faqs form validaition

function removefaqValidation(){
  document.getElementById("img").innerHTML = "";
  document.getElementById("title").innerText = " ";
  document.getElementById("desc").innerText = " ";
  document.getElementById("statuss").innerText = "";

}

function faqValidation() {
  var namess = document.faqform.name.value;
  var emails = document.faqform.email.value;
  var messages = document.faqform.message.value;
  var statuss = document.faqform.btnradio.value;
  

  if (namess == null || namess == "") {
    document.getElementById("namess").innerHTML = "Fill in the fields";
    return false;
  }
  else if (emails == null || emails == "") {
    document.getElementById("emails").innerText = "required ";
    return false;
  }
  else if (messages == null || messages == "") {
    document.getElementById("messages").innerText = "required ";
    return false;
  } 
  else if (statuss == null || statuss == "") {
    document.getElementById("statuss").innerText = "required";
    return false;
  } 

}




//! blog form validaition

function removefaqValidation(){
  document.getElementById("img").innerHTML = "";
  document.getElementById("title").innerText = " ";
  document.getElementById("desc").innerText = " ";
  document.getElementById("statuss").innerText = "";

}

function faqValidation() {
  var namess = document.faqform.name.value;
  var emails = document.faqform.email.value;
  var messages = document.faqform.message.value;
  var statuss = document.faqform.btnradio.value;
  

  if (namess == null || namess == "") {
    document.getElementById("namess").innerHTML = "Fill in the fields";
    return false;
  }
  else if (emails == null || emails == "") {
    document.getElementById("emails").innerText = "required ";
    return false;
  }
  else if (messages == null || messages == "") {
    document.getElementById("messages").innerText = "required ";
    return false;
  } 
  else if (statuss == null || statuss == "") {
    document.getElementById("statuss").innerText = "required";
    return false;
  } 

}
