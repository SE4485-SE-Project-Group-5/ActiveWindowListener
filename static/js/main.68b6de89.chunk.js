(this["webpackJsonpreact-ui"]=this["webpackJsonpreact-ui"]||[]).push([[0],{31:function(e,t,a){e.exports=a(47)},36:function(e,t,a){},37:function(e,t,a){},38:function(e,t,a){},39:function(e,t,a){},40:function(e,t,a){},41:function(e,t,a){},47:function(e,t,a){"use strict";a.r(t);var n=a(0),o=a.n(n),s=a(28),c=a.n(s);a(36),Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));a(37);var r=a(17),l=a(12),i=a(5),m=a(13),u=a(14),d=a(15),h=(a(38),a(16)),g=function(e){function t(e){var a;return Object(l.a)(this,t),(a=Object(m.a)(this,Object(u.a)(t).call(this,e))).state={ws:new WebSocket(a.props.url,a.props.protocol),attempts:1},a.sendMessage=a.sendMessage.bind(Object(h.a)(a)),a.setupWebsocket=a.setupWebsocket.bind(Object(h.a)(a)),a}return Object(d.a)(t,e),Object(i.a)(t,[{key:"logging",value:function(e){!0===this.props.debug&&console.log(e)}},{key:"generateInterval",value:function(e){return this.props.reconnectIntervalInMilliSeconds>0?this.props.reconnectIntervalInMilliSeconds:1e3*Math.min(30,Math.pow(2,e)-1)}},{key:"setupWebsocket",value:function(){var e=this,t=this.state.ws;t.onopen=function(){e.logging("Websocket connected"),"function"===typeof e.props.onOpen&&e.props.onOpen()},t.onmessage=function(t){console.log(t.data),e.props.onMessage(t.data)},this.shouldReconnect=this.props.reconnect,t.onclose=function(){if(e.logging("Websocket disconnected"),"function"===typeof e.props.onClose&&e.props.onClose(),e.shouldReconnect){var t=e.generateInterval(e.state.attempts);e.timeoutID=setTimeout((function(){e.setState({attempts:e.state.attempts+1}),e.setState({ws:new WebSocket(e.props.url,e.props.protocol)}),e.setupWebsocket()}),t)}},t.onerror=function(a){console.log("++++++++++++++++++"),console.log("ERROR WS: ",t.readyState),console.log(e.props.url),console.log("++++++++++++++++++")}}},{key:"componentDidMount",value:function(){this.setupWebsocket()}},{key:"componentWillUnmount",value:function(){this.shouldReconnect=!1,clearTimeout(this.timeoutID),this.state.ws.close()}},{key:"sendMessage",value:function(e){var t=this.state.ws;e=JSON.stringify(e),t.send(e)}},{key:"render",value:function(){return o.a.createElement(n.Fragment,null)}}]),t}(o.a.Component);g.defaultProps={debug:!1,reconnect:!0};var p=g,v=function(e){function t(e){var a;return Object(l.a)(this,t),(a=Object(m.a)(this,Object(u.a)(t).call(this,e))).handleData=function(e){console.log("Data received"),console.log(e)},a.handleOpen=function(){console.log("Connected to Server")},a.handleClose=function(){console.log("Disconnected from Server")},a.sendMessage=function(e){a.refWebSocket.sendMessage(e)},a.SERVER_URL="ws://localhost:43968/example_ws/echo-example",a}return Object(d.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){var e=this;return o.a.createElement("div",{className:"WebSocketExample"},o.a.createElement("button",{onClick:function(){return e.sendMessage("Hello World!")}},"Send Message"),o.a.createElement(p,{url:this.SERVER_URL,onMessage:this.handleData,onOpen:this.handleOpen,onClose:this.handleClose,reconnect:!0,debug:!0,ref:function(t){e.refWebSocket=t}}))}}]),t}(o.a.Component);a(39);var f=function(){return o.a.createElement("div",{className:"NoMatch"},"Sorry, this page doesn't exist. Click Here to Go Back Home.")},E=a(63),b=(a(40),function(e){function t(e){return Object(l.a)(this,t),Object(m.a)(this,Object(u.a)(t).call(this,e))}return Object(d.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){return o.a.createElement("div",{className:"Home"},"HOME PAGE")}}]),t}(n.Component)),C=a(22),k=(a(41),a(62)),P=a(64),w=function(e){function t(e){var a;return Object(l.a)(this,t),(a=Object(m.a)(this,Object(u.a)(t).call(this,e))).handleData=function(e){console.log("Data received"),e=JSON.parse(e),console.log(e),a.setState({data:e})},a.processData=function(e){for(var t=[],n=0,o=Object.entries(e);n<o.length;n++){var s=Object(C.a)(o[n],2),c=s[0],r=s[1];t.push(a.createRow(c,r.icon,[r.mouse_usage,r.keyboard_usage,r.idle,r.open]))}return t},a.handleOpen=function(){console.log("Connected to Server"),a.sendMessage("Hello World!")},a.handleClose=function(){console.log("Disconnected from Server")},a.sendMessage=function(e){a.refWebSocket.sendMessage(e)},a.SERVER_URL="ws://localhost:43968/example_ws/echo-example",a.state={data:{}},a}return Object(d.a)(t,e),Object(i.a)(t,[{key:"createLegend",value:function(){return o.a.createElement(k.a,{container:!0,direction:"row",style:{padding:"5px",marginBottom:"5px"}},o.a.createElement("div",{className:"ChartPage-RowBegin"},o.a.createElement("div",{className:"ChartPage-ItemTitle"},"Legend")),o.a.createElement("div",{className:"ChartPage-Row"},o.a.createElement("div",{className:"ChartPage-ItemPercentsParent"},o.a.createElement("div",{className:"ChartPage-ItemPercents",style:{width:"25%",backgroundColor:"#29B6F6"}},"Mouse Usage In Min"),o.a.createElement("div",{className:"ChartPage-ItemPercents",style:{width:"25%",backgroundColor:"#F9A825"}},"Keyboard Usage In Min"),o.a.createElement("div",{className:"ChartPage-ItemPercents",style:{width:"25%",backgroundColor:"#4CAF50"}},"Idle Time In Min"),o.a.createElement("div",{className:"ChartPage-ItemPercents",style:{width:"25%",backgroundColor:"#f44336"}},"Open Time In Min"))))}},{key:"createRow",value:function(e,t,a){return o.a.createElement(k.a,{container:!0,direction:"row",style:{padding:"5px"},key:e},o.a.createElement("div",{className:"ChartPage-RowBegin"},o.a.createElement("img",{style:{width:"50px",height:"50px"},src:"static/icons/"+t}),o.a.createElement("div",{className:"ChartPage-ItemTitle"},e)),o.a.createElement("div",{className:"ChartPage-Row"},o.a.createElement("div",{className:"ChartPage-ItemPercentsParent"},o.a.createElement("div",{className:"ChartPage-ItemPercents",style:{width:"25%",backgroundColor:"#29B6F6"}},"MU ",a[0]),o.a.createElement("div",{className:"ChartPage-ItemPercents",style:{width:"25%",backgroundColor:"#F9A825"}},"KU ",a[1]),o.a.createElement("div",{className:"ChartPage-ItemPercents",style:{width:"25%",backgroundColor:"#4CAF50"}},"IT ",a[2]),o.a.createElement("div",{className:"ChartPage-ItemPercents",style:{width:"25%",backgroundColor:"#f44336"}},"TT ",a[3]))))}},{key:"render",value:function(){var e=this;return o.a.createElement(P.a,{className:"ChartPage"},this.createLegend(),o.a.createElement("div",{className:"ChartPage-Scroll"},this.processData(this.state.data)),o.a.createElement(P.a,{className:"ChartPage-UserDetails"},o.a.createElement("div",{className:"ChartPage-UserDetails-Title"},"User Details:"),o.a.createElement("div",{className:"ChartPage-UserDetails-Text"},"Username: saran"),o.a.createElement("div",{className:"ChartPage-UserDetails-Text"},"Home Directory: /Users/saran"),o.a.createElement("div",{className:"ChartPage-UserDetails-Text"},"Wifi SSID: CometNet"),o.a.createElement("div",{className:"ChartPage-UserDetails-Text"},"Hostname: cometnet-10-21-79-245.utdallas.edu"),o.a.createElement("div",{className:"ChartPage-UserDetails-Text"},"IP Address: IP Address: 10.21.79.245"),o.a.createElement("div",{className:"ChartPage-UserDetails-Text"},"Mac Address: 82:b9:15:84:94:01")),o.a.createElement(p,{url:this.SERVER_URL,onMessage:this.handleData,onOpen:this.handleOpen,onClose:this.handleClose,reconnect:!0,debug:!0,ref:function(t){e.refWebSocket=t}}))}}]),t}(n.Component);var O=function(){return o.a.createElement(n.Fragment,null,o.a.createElement(E.a,null),o.a.createElement("div",{className:"App"},o.a.createElement(r.c,null,o.a.createElement(r.a,{exact:!0,path:"/",component:w}),o.a.createElement(r.a,{exact:!0,path:"/home",component:b}),o.a.createElement(r.a,{exact:!0,path:"/example",component:v}),o.a.createElement(r.a,{component:f}))))},y=a(23);c.a.render(o.a.createElement(y.a,null,o.a.createElement(O,null)),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()}))}},[[31,1,2]]]);
//# sourceMappingURL=main.68b6de89.chunk.js.map