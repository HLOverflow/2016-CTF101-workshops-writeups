Challenge description:
==
There's a lucky draw at http://web.spro.ink:3007 and the top prize for winning it is a world tour for 2 to anywhere! Too bad I have only two valid coupons :(

Here are two valid coupons for you to start off with:

    GT2498HTFG8347YUHGTF422498JG
    G824989GJG8347DUHGTF4228FDJ3

---
Poking around
==
In this challenge, we test out the webpage to see what is validated. 
We tried to send just the 2 coupons given but receive a message: 
> You need to submit five or more valid coupons in order to win this lucky draw.


We tried sending 2 same coupon and get an error message like this.

> Error: The same coupon cannot be used more than once!

It appears that there are some form of validation before coupons are submitted. We proceed to view html source code and found interesting look scripts that were included in the head section.

view-source:http://web.spro.ink:3007/
```html
  </style>
  <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
  <script src="http://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
  <script src="927RHF82347HF982HF29J83FR9382347FRHG287E43FGH.js" ></script>
</head>
<body>
...
```

We proceed on to view the javascript file and saw all the functions used.

view-source:http://web.spro.ink:3007/927RHF82347HF982HF29J83FR9382347FRHG287E43FGH.js
```javascript
...
function isEverythingOk() {
  if(hasDuplicates()) {
    somethingWrong("The same coupon cannot be used more than once!");
    return false;
  }

  var fields = $(".form-control");
  for(var i=0; i < fields.size(); i++) {
    if(!fields[i].value) continue;
    if(isNotValid(fields[i].value)) {
      somethingWrong("You can only use valid coupons!");
      return false;
    }
  }

  everythingOk();
  return true;
}

function validateAndSubmit() {
  isEverythingOk();
  if(!isFormValidated) {
    return false;
  }

  $("#coupons").submit();
}

function isNotValid(code) {
  return code != 'GT2498HTFG8347YUHGTF422498JG' && code != 'G824989GJG8347DUHGTF4228FDJ3';
}

function hasDuplicates() {
  var fields = $(".form-control");
  var originalSize = fields.size();
  var nonDuplicateCodes = new Set();
  for(var i=0; i < fields.size(); i++) {
    if(!fields[i].value) {
      originalSize -= 1;
      continue;
    }
    nonDuplicateCodes.add(fields[i].value);
  }
  return nonDuplicateCodes.size < originalSize;
}
...
```

After tracing what those functions do, it seems that if we can **overwrite** any of the above function to always return a true/false, we can bypass the validations. 

Exploit
==
I had chosen to overwrite the function ```hasDuplicates()```

So I went to developer tools console, check that the functions are accessible, and overwrite it as the following:
```javascript
	> function hasDuplicates(){ return false }
	undefined
```

Finally, I copy paste the valid coupon 5 times and got the flag!

![screenshot](https://github.com/HLOverflow/2016-CTF101-workshops-writeups/blob/master/challenge8/challenge8.jpg)

---
flag{w3_cre4t3_0uR_Own_1uck}
