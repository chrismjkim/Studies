var Body = {
    setColor: function(color){
      document.querySelector('body').style.color = color;
    },
    setBackgroundColor: function(color){
      document.querySelector('body').style.backgroundColor = color;
    }
  }
  var Links = {
    setLinksColor: function (color) {
      var alist = document.querySelectorAll('a');
      var i = 0;
      while (i < alist.length) {
        alist[i].style.color = color;
        i = i + 1;
      }
    }
  }

  var Button = {
    Chain: function(text) {
      var buttonlist = document.querySelectorAll('input#first');
      var x = 0;
      while (x < buttonlist.length) {
        buttonlist[x].value = text;
        x = x + 1;
      }
    }
  }
    
    function NightDayHandler(self){
    var target = document.querySelector('body');
      if (self.value==='night'){
        Body.setColor('white');
        Body.setBackgroundColor('black');
        Links.setLinksColor('green');
        Button.Chain('day');
      } else {
        Body.setColor('black');
        Body.setBackgroundColor('white');
        Links.setLinksColor('red');
        Button.Chain('night');
      }  
    }