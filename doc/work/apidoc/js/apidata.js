var APIDATA = {
  "api_description" : {
    "title" : "RESTful API",
    "summary" : "This RESTful API document is generated by <a class=\"wistool\" href=\"https://github.com/wisdomtool/rest-client\">WisdomTool REST Client."
  },
  "api_list" : [ {
    "api_summary" : {
      "title" : "Create user",
      "method" : "POST",
      "path" : "/user/F1005"
    },
    "api_request" : {
      "header" : "Accept : application/json,application/xml,application/xhtml+xml,text/html,text/xml,text/plain\r\nContent-Type : application/json; charset=UTF-8\r\n",
      "model" : "   phone [string]\r\n   userName [string]\r\n   userPwd [string]\r\n   email [string]\r\n",
      "example" : "{\n  &quot;phone&quot;: &quot;15921998160&quot;,\n  &quot;userName&quot;: &quot;&#21016;&#32431;&#21326;&quot;,\n  &quot;userPwd&quot;: &quot;123456&quot;,\n  &quot;email&quot;: &quot;lch@163.com&quot;\n}"
    },
    "api_response" : [ {
      "status" : "HTTP/1.0 200 ",
      "code" : 200,
      "message" : "OK",
      "model" : "   count [number]\r\n   datas [array]\r\n    &#9500;&#9472;&#9472;keyId [string]\r\n   message [string]\r\n   status [number]\r\n",
      "example" : "{\n  &quot;count&quot;: 1,\n  &quot;datas&quot;: [\n    {\n      &quot;keyId&quot;: &quot;UR20180108141446428276S6MI&quot;\n    }\n  ],\n  &quot;message&quot;: &quot;&#27880;&#20876;&#25104;&#21151;&quot;,\n  &quot;status&quot;: 0\n}"
    }, {
      "status" : "HTTP/1.0 200 ",
      "code" : 200,
      "message" : "OK",
      "model" : "   count [number]\r\n   datas [array]\r\n   message [string]\r\n   status [number]\r\n",
      "example" : "{\n  &quot;count&quot;: 0,\n  &quot;datas&quot;: [],\n  &quot;message&quot;: &quot;&#27880;&#20876;&#22833;&#36133;,&#35813;&#25163;&#26426;&#21495;&#24050;&#27880;&#20876;&quot;,\n  &quot;status&quot;: -1\n}"
    } ]
  }, {
    "api_summary" : {
      "title" : "Create user",
      "method" : "POST",
      "path" : "/user/F1007"
    },
    "api_request" : {
      "header" : "Accept : application/json,application/xml,application/xhtml+xml,text/html,text/xml,text/plain\r\nContent-Type : application/json; charset=UTF-8\r\n",
      "model" : "   phone [string]\r\n   userPwd [string]\r\n",
      "example" : "{\n  &quot;phone&quot;: &quot;15921998160&quot;,\n  &quot;userPwd&quot;: &quot;123456&quot;\n}"
    },
    "api_response" : [ {
      "status" : "HTTP/1.0 200 ",
      "code" : 200,
      "message" : "OK",
      "model" : "   count [number]\r\n   datas [array]\r\n   message [string]\r\n   status [number]\r\n",
      "example" : "{\n  &quot;count&quot;: 0,\n  &quot;datas&quot;: [],\n  &quot;message&quot;: &quot;&#30331;&#24405;&#25104;&#21151;&quot;,\n  &quot;status&quot;: 0\n}"
    }, {
      "status" : "HTTP/1.0 200 ",
      "code" : 200,
      "message" : "OK",
      "model" : "   count [number]\r\n   datas [array]\r\n   message [string]\r\n   status [number]\r\n",
      "example" : "{\n  &quot;count&quot;: 0,\n  &quot;datas&quot;: [],\n  &quot;message&quot;: &quot;&#35813;&#29992;&#25143;&#26410;&#27880;&#20876;&quot;,\n  &quot;status&quot;: -1\n}"
    } ]
  }, {
    "api_summary" : {
      "title" : "Create user",
      "method" : "POST",
      "path" : "/user/F1008"
    },
    "api_request" : {
      "header" : "Accept : application/json,application/xml,application/xhtml+xml,text/html,text/xml,text/plain\r\nContent-Type : application/json; charset=UTF-8\r\n",
      "model" : "   phone [string]\r\n   userPwd [string]\r\n",
      "example" : "{\n  &quot;phone&quot;: &quot;1592199816&quot;,\n  &quot;userPwd&quot;: &quot;123456&quot;\n}"
    },
    "api_response" : [ {
      "status" : null,
      "code" : 0,
      "message" : "",
      "model" : "N/A",
      "example" : "N/A"
    }, {
      "status" : "HTTP/1.0 200 ",
      "code" : 200,
      "message" : "OK",
      "model" : "   count [number]\r\n   datas [array]\r\n   message [string]\r\n   status [number]\r\n",
      "example" : "{\n  &quot;count&quot;: 0,\n  &quot;datas&quot;: [],\n  &quot;message&quot;: &quot;&#30331;&#20986;&#22833;&#36133;&quot;,\n  &quot;status&quot;: -1\n}"
    }, {
      "status" : "HTTP/1.0 200 ",
      "code" : 200,
      "message" : "OK",
      "model" : "   count [number]\r\n   datas [array]\r\n   message [string]\r\n   status [number]\r\n",
      "example" : "{\n  &quot;count&quot;: 0,\n  &quot;datas&quot;: [],\n  &quot;message&quot;: &quot;&#30331;&#20986;&#25104;&#21151;&quot;,\n  &quot;status&quot;: 0\n}"
    }, {
      "status" : "HTTP/1.0 500 ",
      "code" : 500,
      "message" : "Internal Server Error",
      "model" : "",
      "example" : "&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 3.2 Final//EN&quot;&gt;\n&lt;title&gt;500 Internal Server Error&lt;/title&gt;\n&lt;h1&gt;Internal Server Error&lt;/h1&gt;\n&lt;p&gt;The server encountered an internal error and was unable to complete your request.  Either the server is overloaded or there is an error in the application.&lt;/p&gt;\n"
    } ]
  } ]
};
