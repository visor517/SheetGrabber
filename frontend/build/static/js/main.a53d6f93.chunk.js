(this.webpackJsonppanda=this.webpackJsonppanda||[]).push([[0],{26:function(e,t,n){},6:function(e,t,n){e.exports={ascending:"ColName_ascending__2NuGR",descending:"ColName_descending__262gK",pointer:"ColName_pointer__3WTRy"}},69:function(e,t,n){"use strict";n.r(t);var c=n(1),r=n.n(c),i=n(20),s=n.n(i),a=(n(26),n(27),n(28),n(9)),o=n(3),u=n(21),j=n.n(u),l=n(6),b=n.n(l),d=n(0);function O(e){var t=e.keyName,n=e.onClick,c=e.arrow,r=[b.a.pointer];return!0===c&&r.push(b.a.ascending),!1===c&&r.push(b.a.descending),Object(d.jsx)("th",{scope:"col",className:r.join(" "),onClick:function(){return n(t)},children:t})}function f(e){var t=e.numRows,n=e.rowsLimit,c=e.activePage,r=e.setPageNum,i=[],s=0;do{s++,i.push(s)}while(s*n<t);return Object(d.jsx)("nav",{"aria-label":"Page navigation",className:"d-flex justify-content-center",children:Object(d.jsx)("ul",{className:"pagination",children:i.filter((function(e){return!(i.length>11&&1!==e&&e!==i.length&&(e<c-4||e>c+4))})).map((function(e,t){var n="page-item";return e===c&&(n+=" active"),Object(d.jsx)("li",{className:n,children:Object(d.jsx)("button",{className:"page-link",onClick:function(t){return function(e,t){r(t),e.target.blur()}(t,e)},children:e})},t)}))})})}function h(e){var t=e.onChange;return Object(d.jsxs)("div",{children:[Object(d.jsx)("span",{children:"\u0424\u0438\u043b\u044c\u0442\u0440: "}),Object(d.jsx)("input",{onChange:function(e){return t(e.target.value.toLowerCase())}})]})}function g(e){var t=e.limit,n=e.setLimit;return Object(d.jsxs)("div",{children:["10 - 100 :",Object(d.jsx)("input",{type:"number",min:"10",max:"100",className:"ms-2",defaultValue:t,onChange:function(e){var t;(t=e.target.value)>=10&&t<=100&&n(t)}})]})}function m(e){var t=e.item;return Object(d.jsx)("tr",{children:Object.values(t).map((function(e,t){return Object(d.jsx)("td",{children:String(e)},t)}))})}var x=function(){var e=Object(c.useState)([]),t=Object(o.a)(e,2),n=t[0],r=t[1],i=Object(c.useState)([]),s=Object(o.a)(i,2),u=s[0],l=s[1],b=Object(c.useState)(1),x=Object(o.a)(b,2),p=x[0],v=x[1],y=Object(c.useState)(50),N=Object(o.a)(y,2),C=N[0],w=N[1],k=Object(c.useState)(""),S=Object(o.a)(k,2),B=S[0],I=S[1],_=Object(c.useState)({sortBy:void 0,isIncrease:!0}),L=Object(o.a)(_,2),P=L[0],E=L[1];function F(e){P.sortBy===e?E((function(e){return Object(a.a)(Object(a.a)({},e),{},{isIncrease:!e.isIncrease})})):E({sortBy:e,isIncrease:!0})}function R(){j()("http://127.0.0.1:8000/api/orders/").then((function(e){return r(e.data)}),(function(e){return console.log("\u041e\u0448\u0438\u0431\u043a\u0430 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f \u0434\u0430\u043d\u043d\u044b\u0445")}))}return Object(c.useEffect)(R,[]),setInterval(R,3e3),Object(c.useEffect)((function(){l(n.filter((function(e){return Object.values(e).filter((function(e){return null!=e&&-1!==e.toString().toLowerCase().indexOf(B)})).length>0})).sort((function(e,t){return P.isIncrease?e[P.sortBy]<t[P.sortBy]?-1:1:e[P.sortBy]>t[P.sortBy]?-1:1})))}),[n,B,P]),Object(c.useEffect)((function(){return v(1)}),[C,u]),Object(d.jsx)("div",{className:"container bg-light shadow bg-body rounded",children:Object(d.jsx)("div",{className:"row",children:Object(d.jsxs)("div",{className:"col p-3",children:[Object(d.jsxs)("div",{className:"d-flex justify-content-between",children:[Object(d.jsx)(h,{onChange:I}),Object(d.jsx)(g,{limit:C,setLimit:w})]}),n.length>0?Object(d.jsxs)("table",{className:"table",children:[Object(d.jsx)("thead",{children:Object(d.jsx)("tr",{children:Object.keys(n[0]).map((function(e){var t=e===P.sortBy?P.isIncrease:void 0;return Object(d.jsx)(O,{keyName:e,onClick:F,arrow:t},e)}))})}),Object(d.jsx)("tbody",{children:u.length>0?u.filter((function(e,t){return t>=(p-1)*C&&t<p*C})).map((function(e){return Object(d.jsx)(m,{item:e},e.id)})):Object(d.jsx)("tr",{children:Object(d.jsx)("td",{colSpan:Object.keys(n[0]).length,children:"\u041d\u0435\u0442 \u0434\u0430\u043d\u043d\u044b\u0445"})})})]}):Object(d.jsx)("p",{children:"\u0417\u0430\u0433\u0440\u0443\u0436\u0430\u0435\u0442\u0441\u044f..."}),Object(d.jsx)(f,{numRows:u.length,rowsLimit:C,activePage:p,setPageNum:v})]})})})},p=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,70)).then((function(t){var n=t.getCLS,c=t.getFID,r=t.getFCP,i=t.getLCP,s=t.getTTFB;n(e),c(e),r(e),i(e),s(e)}))};s.a.render(Object(d.jsx)(r.a.StrictMode,{children:Object(d.jsx)(x,{})}),document.getElementById("root")),p()}},[[69,1,2]]]);
//# sourceMappingURL=main.a53d6f93.chunk.js.map