function dv_rolloutManager(handlersDefsArray, baseHandler) {
    this.handle = function () {
        var errorsArr = [];

        var handler = chooseEvaluationHandler(handlersDefsArray);
        if (handler) {
            var errorObj = handleSpecificHandler(handler);
            if (errorObj === null) {
                return errorsArr;
            }
            else {
                var debugInfo = handler.onFailure();
                if (debugInfo) {
                    for (var key in debugInfo) {
                        if (debugInfo.hasOwnProperty(key)) {
                            if (debugInfo[key] !== undefined || debugInfo[key] !== null) {
                                errorObj[key] = encodeURIComponent(debugInfo[key]);
                            }
                        }
                    }
                }
                errorsArr.push(errorObj);
            }
        }

        var errorObjHandler = handleSpecificHandler(baseHandler);
        if (errorObjHandler) {
            errorObjHandler['dvp_isLostImp'] = 1;
            errorsArr.push(errorObjHandler);
        }
        return errorsArr;
    };

    function handleSpecificHandler(handler) {
        var request;
        var errorObj = null;

        try {
            request = handler.createRequest();
            if (request && !request.isSev1) {
                var url = request.url || request;
                if (url) {
                    if (!handler.sendRequest(url)) {
                        errorObj = createAndGetError('sendRequest failed.',
                            url,
                            handler.getVersion(),
                            handler.getVersionParamName(),
                            handler.dv_script);
                    }
                } else {
                    errorObj = createAndGetError('createRequest failed.',
                        url,
                        handler.getVersion(),
                        handler.getVersionParamName(),
                        handler.dv_script,
                        handler.dvScripts,
                        handler.dvStep,
                        handler.dvOther
                    );
                }
            }
        }
        catch (e) {
            errorObj = createAndGetError(e.name + ': ' + e.message, request ? (request.url || request) : null, handler.getVersion(), handler.getVersionParamName(), (handler ? handler.dv_script : null));
        }

        return errorObj;
    }

    function createAndGetError(error, url, ver, versionParamName, dv_script, dvScripts, dvStep, dvOther) {
        var errorObj = {};
        errorObj[versionParamName] = ver;
        errorObj['dvp_jsErrMsg'] = encodeURIComponent(error);
        if (dv_script && dv_script.parentElement && dv_script.parentElement.tagName && dv_script.parentElement.tagName == 'HEAD') {
            errorObj['dvp_isOnHead'] = '1';
        }
        if (url) {
            errorObj['dvp_jsErrUrl'] = url;
        }
        if (dvScripts) {
            var dvScriptsResult = '';
            for (var id in dvScripts) {
                if (dvScripts[id] && dvScripts[id].src) {
                    dvScriptsResult += encodeURIComponent(dvScripts[id].src) + ":" + dvScripts[id].isContain + ",";
                }
            }
            
            
            
        }
        return errorObj;
    }

    function chooseEvaluationHandler(handlersArray) {
        var config = window._dv_win.dv_config;
        var index = 0;
        var isEvaluationVersionChosen = false;
        if (config.handlerVersionSpecific) {
            for (var i = 0; i < handlersArray.length; i++) {
                if (handlersArray[i].handler.getVersion() == config.handlerVersionSpecific) {
                    isEvaluationVersionChosen = true;
                    index = i;
                    break;
                }
            }
        }
        else if (config.handlerVersionByTimeIntervalMinutes) {
            var date = config.handlerVersionByTimeInputDate || new Date();
            var hour = date.getUTCHours();
            var minutes = date.getUTCMinutes();
            index = Math.floor(((hour * 60) + minutes) / config.handlerVersionByTimeIntervalMinutes) % (handlersArray.length + 1);
            if (index != handlersArray.length) { 
                isEvaluationVersionChosen = true;
            }
        }
        else {
            var rand = config.handlerVersionRandom || (Math.random() * 100);
            for (var i = 0; i < handlersArray.length; i++) {
                if (rand >= handlersArray[i].minRate && rand < handlersArray[i].maxRate) {
                    isEvaluationVersionChosen = true;
                    index = i;
                    break;
                }
            }
        }

        if (isEvaluationVersionChosen == true && handlersArray[index].handler.isApplicable()) {
            return handlersArray[index].handler;
        }
        else {
            return null;
        }
    }
}

function doesBrowserSupportHTML5Push() {
    "use strict";
    return typeof window.parent.postMessage === 'function' && window.JSON;
}

function dv_GetParam(url, name, checkFromStart) {
    name = name.replace(/[\[]/, "\\\[").replace(/[\]]/, "\\\]");
    var regexS = (checkFromStart ? "(?:\\?|&|^)" : "[\\?&]") + name + "=([^&#]*)";
    var regex = new RegExp(regexS, 'i');
    var results = regex.exec(url);
    if (results == null)
        return null;
    else
        return results[1];
}

function dv_Contains(array, obj) {
    var i = array.length;
    while (i--) {
        if (array[i] === obj) {
            return true;
        }
    }
    return false;
}

function dv_GetDynamicParams(url) {
    try {
        var regex = new RegExp("[\\?&](dvp_[^&]*=[^&#]*)", "gi");
        var dvParams = regex.exec(url);

        var results = new Array();
        while (dvParams != null) {
            results.push(dvParams[1]);
            dvParams = regex.exec(url);
        }
        return results;
    }
    catch (e) {
        return [];
    }
}

function dv_createIframe() {
    var iframe;
    if (document.createElement && (iframe = document.createElement('iframe'))) {
        iframe.name = iframe.id = 'iframe_' + Math.floor((Math.random() + "") * 1000000000000);
        iframe.width = 0;
        iframe.height = 0;
        iframe.style.display = 'none';
        iframe.src = 'about:blank';
    }

    return iframe;
}

function dv_GetRnd() {
    return ((new Date()).getTime() + "" + Math.floor(Math.random() * 1000000)).substr(0, 16);
}

function dv_SendErrorImp(serverUrl, errorsArr) {

    for (var j = 0; j < errorsArr.length; j++) {
        var errorObj = errorsArr[j];
        var errorImp = dv_CreateAndGetErrorImp(serverUrl, errorObj);
        dv_sendImgImp(errorImp);
    }
}

function dv_CreateAndGetErrorImp(serverUrl, errorObj) {
    var errorQueryString = '';
    for (key in errorObj) {
        if (errorObj.hasOwnProperty(key)) {
            if (key.indexOf('dvp_jsErrUrl') == -1) {
                errorQueryString += '&' + key + '=' + errorObj[key];
            }
            else {
                var params = ['ctx', 'cmp', 'plc', 'sid'];
                for (var i = 0; i < params.length; i++) {
                    var pvalue = dv_GetParam(errorObj[key], params[i]);
                    if (pvalue) {
                        errorQueryString += '&dvp_js' + params[i] + '=' + pvalue;
                    }
                }
            }
        }
    }

    var windowProtocol = 'https:';
    var sslFlag = '&ssl=1';

    var errorImp = windowProtocol + '//' + serverUrl + sslFlag + errorQueryString;
    return errorImp;
}

function dv_sendImgImp(url) {
    (new Image()).src = url;
}

function dv_sendScriptRequest(url) {
    document.write('<scr' + 'ipt type="text/javascript" src="' + url + '"></scr' + 'ipt>');
}

function dv_getPropSafe(obj, propName) {
    try {
        if (obj)
            return obj[propName];
    } catch (e) {
    }
}

function dvBsType() {
    var that = this;
    var eventsForDispatch = {};
    this.t2tEventDataZombie = {};

    this.processT2TEvent = function (data, tag) {
        try {
            if (tag.ServerPublicDns) {
                data.timeStampCollection.push({"beginProcessT2TEvent": getCurrentTime()});
                data.timeStampCollection.push({'beginVisitCallback': tag.beginVisitCallbackTS});
                var tpsServerUrl = tag.dv_protocol + '//' + tag.ServerPublicDns + '/event.gif?impid=' + tag.uid;

                if (!tag.uniquePageViewId) {
                    tag.uniquePageViewId = data.uniquePageViewId;
                }

                tpsServerUrl += '&dvp_upvid=' + tag.uniquePageViewId;
                tpsServerUrl += '&dvp_numFrames=' + data.totalIframeCount;
                tpsServerUrl += '&dvp_numt2t=' + data.totalT2TiframeCount;
                tpsServerUrl += '&dvp_frameScanDuration=' + data.scanAllFramesDuration;
                tpsServerUrl += '&dvp_scene=' + tag.adServingScenario;
                tpsServerUrl += '&dvp_ist2twin=' + (data.isWinner ? '1' : '0');
                tpsServerUrl += '&dvp_numTags=' + Object.keys($dvbs.tags).length;
                tpsServerUrl += '&dvp_isInSample=' + data.isInSample;
                tpsServerUrl += (data.wasZombie) ? '&dvp_wasZombie=1' : '&dvp_wasZombie=0';
                tpsServerUrl += '&dvp_ts_t2tCreatedOn=' + data.creationTime;
                if (data.timeStampCollection) {
                    if (window._dv_win.t2tTimestampData) {
                        for (var tsI = 0; tsI < window._dv_win.t2tTimestampData.length; tsI++) {
                            data.timeStampCollection.push(window._dv_win.t2tTimestampData[tsI]);
                        }
                    }

                    for (var i = 0; i < data.timeStampCollection.length; i++) {
                        var item = data.timeStampCollection[i];
                        for (var propName in item) {
                            if (item.hasOwnProperty(propName)) {
                                tpsServerUrl += '&dvp_ts_' + propName + '=' + item[propName];
                            }
                        }
                    }
                }
                $dvbs.domUtilities.addImage(tpsServerUrl, tag.tagElement.parentElement);
            }
        } catch (e) {
            try {
                dv_SendErrorImp(window._dv_win.dv_config.tpsErrAddress + '/visit.jpg?ctx=818052&cmp=1619415&dvtagver=6.1.src&jsver=0&dvp_ist2tProcess=1', {dvp_jsErrMsg: encodeURIComponent(e)});
            } catch (ex) {
            }
        }
    };

    this.processTagToTagCollision = function (collision, tag) {
        var i;
        var tpsServerUrl = tag.dv_protocol + '//' + tag.ServerPublicDns + '/event.gif?impid=' + tag.uid;
        var additions = [
            '&dvp_collisionReasons=' + collision.reasonBitFlag,
            '&dvp_ts_reporterDvTagCreated=' + collision.thisTag.dvTagCreatedTS,
            '&dvp_ts_reporterVisitJSMessagePosted=' + collision.thisTag.visitJSPostMessageTS,
            '&dvp_ts_reporterReceivedByT2T=' + collision.thisTag.receivedByT2TTS,
            '&dvp_ts_collisionPostedFromT2T=' + collision.postedFromT2TTS,
            '&dvp_ts_collisionReceivedByCommon=' + collision.commonRecievedTS,
            '&dvp_collisionTypeId=' + collision.allReasonsForTagBitFlag
        ];
        tpsServerUrl += additions.join("");

        for (i = 0; i < collision.reasons.length; i++) {
            var reason = collision.reasons[i];
            tpsServerUrl += '&dvp_' + reason + "MS=" + collision[reason + "MS"];
        }

        if (tag.uniquePageViewId) {
            tpsServerUrl += '&dvp_upvid=' + tag.uniquePageViewId;
        }
        $dvbs.domUtilities.addImage(tpsServerUrl, tag.tagElement.parentElement);
    };

    var messageEventListener = function (event) {
        try {
            var timeCalled = getCurrentTime();
            var data = window.JSON.parse(event.data);
            if (!data.action) {
                data = window.JSON.parse(data);
            }
            if (data.timeStampCollection) {
                data.timeStampCollection.push({messageEventListenerCalled: timeCalled});
            }
            var myUID;
            var visitJSHasBeenCalledForThisTag = false;
            if ($dvbs.tags) {
                for (var uid in $dvbs.tags) {
                    if ($dvbs.tags.hasOwnProperty(uid) && $dvbs.tags[uid] && $dvbs.tags[uid].t2tIframeId === data.iFrameId) {
                        myUID = uid;
                        visitJSHasBeenCalledForThisTag = true;
                        break;
                    }
                }
            }

            switch (data.action) {
                case 'uniquePageViewIdDetermination' :
                    if (visitJSHasBeenCalledForThisTag) {
                        $dvbs.processT2TEvent(data, $dvbs.tags[myUID]);
                        $dvbs.t2tEventDataZombie[data.iFrameId] = undefined;
                    }
                    else {
                        data.wasZombie = 1;
                        $dvbs.t2tEventDataZombie[data.iFrameId] = data;
                    }
                    break;
                case 'maColl':
                    var tag = $dvbs.tags[myUID];
                    
                    tag.AdCollisionMessageRecieved = true;
                    if (!tag.uniquePageViewId) {
                        tag.uniquePageViewId = data.uniquePageViewId;
                    }
                    data.collision.commonRecievedTS = timeCalled;
                    $dvbs.processTagToTagCollision(data.collision, tag);
                    break;
            }

        } catch (e) {
            try {
                dv_SendErrorImp(window._dv_win.dv_config.tpsErrAddress + '/visit.jpg?ctx=818052&cmp=1619415&dvtagver=6.1.src&jsver=0&dvp_ist2tListener=1', {dvp_jsErrMsg: encodeURIComponent(e)});
            } catch (ex) {
            }
        }
    };

    if (window.addEventListener)
        addEventListener("message", messageEventListener, false);
    else
        attachEvent("onmessage", messageEventListener);

    this.pubSub = new function () {

        var subscribers = [];

        this.subscribe = function (eventName, uid, actionName, func) {
            if (!subscribers[eventName + uid])
                subscribers[eventName + uid] = [];
            subscribers[eventName + uid].push({Func: func, ActionName: actionName});
        };

        this.publish = function (eventName, uid) {
            var actionsResults = [];
            if (eventName && uid && subscribers[eventName + uid] instanceof Array)
                for (var i = 0; i < subscribers[eventName + uid].length; i++) {
                    var funcObject = subscribers[eventName + uid][i];
                    if (funcObject && funcObject.Func && typeof funcObject.Func == "function" && funcObject.ActionName) {
                        var isSucceeded = runSafely(function () {
                            return funcObject.Func(uid);
                        });
                        actionsResults.push(encodeURIComponent(funcObject.ActionName) + '=' + (isSucceeded ? '1' : '0'));
                    }
                }
            return actionsResults.join('&');
        };
    };

    this.domUtilities = new function () {

        this.addImage = function (url, parentElement) {
            var image = parentElement.ownerDocument.createElement("img");
            image.width = 0;
            image.height = 0;
            image.style.display = 'none';
            image.src = appendCacheBuster(url);
            parentElement.insertBefore(image, parentElement.firstChild);
        };

        this.addScriptResource = function (url, parentElement) {
            if (parentElement) {
                var scriptElem = parentElement.ownerDocument.createElement("script");
                scriptElem.type = 'text/javascript';
                scriptElem.src = appendCacheBuster(url);
                parentElement.insertBefore(scriptElem, parentElement.firstChild);
            }
            else {
                addScriptResourceFallBack(url);
            }
        };

        function addScriptResourceFallBack(url) {
            var scriptElem = document.createElement('script');
            scriptElem.type = "text/javascript";
            scriptElem.src = appendCacheBuster(url);
            var firstScript = document.getElementsByTagName('script')[0];
            firstScript.parentNode.insertBefore(scriptElem, firstScript);
        }

        this.addScriptCode = function (srcCode, parentElement) {
            var scriptElem = parentElement.ownerDocument.createElement("script");
            scriptElem.type = 'text/javascript';
            scriptElem.innerHTML = srcCode;
            parentElement.insertBefore(scriptElem, parentElement.firstChild);
        };

        this.addHtml = function (srcHtml, parentElement) {
            var divElem = parentElement.ownerDocument.createElement("div");
            divElem.style = "display: inline";
            divElem.innerHTML = srcHtml;
            parentElement.insertBefore(divElem, parentElement.firstChild);
        };
    };

    this.resolveMacros = function (str, tag) {
        var viewabilityData = tag.getViewabilityData();
        var viewabilityBuckets = viewabilityData && viewabilityData.buckets ? viewabilityData.buckets : {};
        var upperCaseObj = objectsToUpperCase(tag, viewabilityData, viewabilityBuckets);
        var newStr = str.replace('[DV_PROTOCOL]', upperCaseObj.DV_PROTOCOL);
        newStr = newStr.replace('[PROTOCOL]', upperCaseObj.PROTOCOL);
        newStr = newStr.replace(/\[(.*?)\]/g, function (match, p1) {
            var value = upperCaseObj[p1];
            if (value === undefined || value === null)
                value = '[' + p1 + ']';
            return encodeURIComponent(value);
        });
        return newStr;
    };

    this.settings = new function () {
    };

    this.tagsType = function () {
    };

    this.tagsPrototype = function () {
        this.add = function (tagKey, obj) {
            if (!that.tags[tagKey])
                that.tags[tagKey] = new that.tag();
            for (var key in obj)
                that.tags[tagKey][key] = obj[key];
        };
    };

    this.tagsType.prototype = new this.tagsPrototype();
    this.tagsType.prototype.constructor = this.tags;
    this.tags = new this.tagsType();

    this.tag = function () {
    };
    this.tagPrototype = function () {
        this.set = function (obj) {
            for (var key in obj)
                this[key] = obj[key];
        };

        this.getViewabilityData = function () {
        };
    };

    this.tag.prototype = new this.tagPrototype();
    this.tag.prototype.constructor = this.tag;

    this.getTagObjectByService = function (serviceName) {

        for (var impressionId in this.tags) {
            if (typeof this.tags[impressionId] === 'object'
                && this.tags[impressionId].services
                && this.tags[impressionId].services[serviceName]
                && !this.tags[impressionId].services[serviceName].isProcessed) {
                this.tags[impressionId].services[serviceName].isProcessed = true;
                return this.tags[impressionId];
            }
        }


        return null;
    };

    this.addService = function (impressionId, serviceName, paramsObject) {

        if (!impressionId || !serviceName)
            return;

        if (!this.tags[impressionId])
            return;
        else {
            if (!this.tags[impressionId].services)
                this.tags[impressionId].services = {};

            this.tags[impressionId].services[serviceName] = {
                params: paramsObject,
                isProcessed: false
            };
        }
    };

    this.Enums = {
        BrowserId: {Others: 0, IE: 1, Firefox: 2, Chrome: 3, Opera: 4, Safari: 5},
        TrafficScenario: {OnPage: 1, SameDomain: 2, CrossDomain: 128}
    };

    this.CommonData = {};

    var runSafely = function (action) {
        try {
            var ret = action();
            return ret !== undefined ? ret : true;
        } catch (e) {
            return false;
        }
    };

    var objectsToUpperCase = function () {
        var upperCaseObj = {};
        for (var i = 0; i < arguments.length; i++) {
            var obj = arguments[i];
            for (var key in obj) {
                if (obj.hasOwnProperty(key)) {
                    upperCaseObj[key.toUpperCase()] = obj[key];
                }
            }
        }
        return upperCaseObj;
    };

    var appendCacheBuster = function (url) {
        if (url !== undefined && url !== null && url.match("^http") == "http") {
            if (url.indexOf('?') !== -1) {
                if (url.slice(-1) == '&')
                    url += 'cbust=' + dv_GetRnd();
                else
                    url += '&cbust=' + dv_GetRnd();
            }
            else
                url += '?cbust=' + dv_GetRnd();
        }
        return url;
    };

    
    this.messages = new function () {
        var waitingMessages = [];
        var waitingCallbacks = [];

        this.registerMsg = function(dvFrame, data) {
            if (!waitingMessages[dvFrame]) {
                waitingMessages[dvFrame] = [];
            }

            waitingMessages[dvFrame].push(data);

            if (dvFrame.$uid) {
                sendWaitingEventsForFrame(dvFrame, dvFrame.$uid);
            }
        };

        this.startSendingEvents = function(dvFrame, impID) {
            sendWaitingEventsForFrame(dvFrame, impID);
            
        };

        function sendWaitingEventsForFrame(dvFrame, impID) {
            if (waitingMessages[dvFrame]) {
                var eventObject = {};
                for (var i = 0; i < waitingMessages[dvFrame].length; i++) {
                    var obj = waitingMessages[dvFrame].pop();
                    for (var key in obj) {
                        if (typeof obj[key] !== 'function' && obj.hasOwnProperty(key)) {
                            eventObject[key] = obj[key];
                        }
                    }
                }
                that.registerEventCall(impID, eventObject);
            }
        }

        function startMessageManager() {
            for (var frm in waitingMessages) {
                if (frm && frm.$uid) {
                    sendWaitingEventsForFrame(frm, frm.$uid);
                }
            }
            setTimeout(startMessageManager, 10);
        }
    };

    this.dispatchRegisteredEventsFromAllTags = function () {
        for (var impressionId in this.tags) {
            if (typeof this.tags[impressionId] !== 'function' && typeof this.tags[impressionId] !== 'undefined')
                dispatchEventCalls(impressionId, this);
        }
    };

    var dispatchEventCalls = function (impressionId, dvObj) {
        var tag = dvObj.tags[impressionId];
        var eventObj = eventsForDispatch[impressionId];
        if (typeof eventObj !== 'undefined' && eventObj != null) {
            var url = tag.protocol + '//' + tag.ServerPublicDns + "/bsevent.gif?impid=" + impressionId + '&' + createQueryStringParams(eventObj);
            dvObj.domUtilities.addImage(url, tag.tagElement.parentElement);
            eventsForDispatch[impressionId] = null;
        }
    };

    this.registerEventCall = function (impressionId, eventObject, timeoutMs) {
        addEventCallForDispatch(impressionId, eventObject);

        if (typeof timeoutMs === 'undefined' || timeoutMs == 0 || isNaN(timeoutMs))
            dispatchEventCallsNow(this, impressionId, eventObject);
        else {
            if (timeoutMs > 2000)
                timeoutMs = 2000;

            var dvObj = this;
            setTimeout(function () {
                dispatchEventCalls(impressionId, dvObj);
            }, timeoutMs);
        }
    };

    var dispatchEventCallsNow = function (dvObj, impressionId, eventObject) {
        addEventCallForDispatch(impressionId, eventObject);
        dispatchEventCalls(impressionId, dvObj);
    };

    var addEventCallForDispatch = function (impressionId, eventObject) {
        for (var key in eventObject) {
            if (typeof eventObject[key] !== 'function' && eventObject.hasOwnProperty(key)) {
                if (!eventsForDispatch[impressionId])
                    eventsForDispatch[impressionId] = {};
                eventsForDispatch[impressionId][key] = eventObject[key];
            }
        }
    };

    if (window.addEventListener) {
        window.addEventListener('unload', function () {
            that.dispatchRegisteredEventsFromAllTags();
        }, false);
        window.addEventListener('beforeunload', function () {
            that.dispatchRegisteredEventsFromAllTags();
        }, false);
    }
    else if (window.attachEvent) {
        window.attachEvent('onunload', function () {
            that.dispatchRegisteredEventsFromAllTags();
        }, false);
        window.attachEvent('onbeforeunload', function () {
            that.dispatchRegisteredEventsFromAllTags();
        }, false);
    }
    else {
        window.document.body.onunload = function () {
            that.dispatchRegisteredEventsFromAllTags();
        };
        window.document.body.onbeforeunload = function () {
            that.dispatchRegisteredEventsFromAllTags();
        };
    }

    var createQueryStringParams = function (values) {
        var params = '';
        for (var key in values) {
            if (typeof values[key] !== 'function') {
                var value = encodeURIComponent(values[key]);
                if (params === '')
                    params += key + '=' + value;
                else
                    params += '&' + key + '=' + value;
            }
        }

        return params;
    };
}

function dv_baseHandler(){function I(e,a){var d=document.createElement("iframe");d.name=window._dv_win.dv_config.emptyIframeID||"iframe_"+J();d.width=0;d.height=0;d.id=a;d.style.display="none";d.src=e;return d}function E(e,a,d){var d=d||150,c=window._dv_win||window;if(c.document&&c.document.body)return a&&a.parentNode?a.parentNode.insertBefore(e,a):c.document.body.insertBefore(e,c.document.body.firstChild),!0;if(0<d)setTimeout(function(){E(e,a,--d)},20);else return!1}function M(e){var a=null;try{if(a=
e&&e.contentDocument)return a}catch(d){}try{if(a=e.contentWindow&&e.contentWindow.document)return a}catch(c){}try{if(a=window._dv_win.frames&&window._dv_win.frames[e.name]&&window._dv_win.frames[e.name].document)return a}catch(b){}return null}function K(e,a,d,c,b,p,u,l,v,s){var f,i,g;void 0==a.dvregion&&(a.dvregion=0);var h,k,m;try{g=c;for(i=0;10>i&&g!=window._dv_win.top;)i++,g=g.parent;c.depth=i;f=N(c);h="&aUrl="+encodeURIComponent(f.url);k="&aUrlD="+f.depth;m=c.depth+b;p&&c.depth--}catch(O){k=h=
m=c.depth=""}void 0!=a.aUrl&&(h="&aUrl="+a.aUrl);b=a.script.src;p="&ctx="+(dv_GetParam(b,"ctx")||"")+"&cmp="+(dv_GetParam(b,"cmp")||"")+"&plc="+(dv_GetParam(b,"plc")||"")+"&sid="+(dv_GetParam(b,"sid")||"")+"&advid="+(dv_GetParam(b,"advid")||"")+"&adsrv="+(dv_GetParam(b,"adsrv")||"")+"&unit="+(dv_GetParam(b,"unit")||"")+"&isdvvid="+(dv_GetParam(b,"isdvvid")||"")+"&uid="+a.uid+"&tagtype="+(dv_GetParam(b,"tagtype")||"")+"&adID="+(dv_GetParam(b,"adID")||"")+"&app="+(dv_GetParam(b,"app")||"")+"&sup="+
(dv_GetParam(b,"sup")||"");(g=dv_GetParam(b,"xff"))&&(p+="&xff="+g);(g=dv_GetParam(b,"useragent"))&&(p+="&useragent="+g);if(void 0!=window._dv_win.$dvbs.CommonData.BrowserId&&void 0!=window._dv_win.$dvbs.CommonData.BrowserVersion&&void 0!=window._dv_win.$dvbs.CommonData.BrowserIdFromUserAgent)f=window._dv_win.$dvbs.CommonData.BrowserId,i=window._dv_win.$dvbs.CommonData.BrowserVersion,g=window._dv_win.$dvbs.CommonData.BrowserIdFromUserAgent;else{var t=g?decodeURIComponent(g):navigator.userAgent;f=
[{id:4,brRegex:"OPR|Opera",verRegex:"(OPR/|Version/)"},{id:1,brRegex:"MSIE|Trident/7.*rv:11|rv:11.*Trident/7|Edge/",verRegex:"(MSIE |rv:| Edge/)"},{id:2,brRegex:"Firefox",verRegex:"Firefox/"},{id:0,brRegex:"Mozilla.*Android.*AppleWebKit(?!.*Chrome.*)|Linux.*Android.*AppleWebKit.* Version/.*Chrome",verRegex:null},{id:0,brRegex:"AOL/.*AOLBuild/|AOLBuild/.*AOL/|Puffin|Maxthon|Valve|Silk|PLAYSTATION|PlayStation|Nintendo|wOSBrowser",verRegex:null},{id:3,brRegex:"Chrome",verRegex:"Chrome/"},{id:5,brRegex:"Safari|(OS |OS X )[0-9].*AppleWebKit",
verRegex:"Version/"}];g=0;i="";for(var r=0;r<f.length;r++)if(null!=t.match(RegExp(f[r].brRegex))){g=f[r].id;if(null==f[r].verRegex)break;t=t.match(RegExp(f[r].verRegex+"[0-9]*"));null!=t&&(i=t[0].match(RegExp(f[r].verRegex)),i=t[0].replace(i[0],""));break}f=r=P();i=r===g?i:"";window._dv_win.$dvbs.CommonData.BrowserId=f;window._dv_win.$dvbs.CommonData.BrowserVersion=i;window._dv_win.$dvbs.CommonData.BrowserIdFromUserAgent=g}p+="&brid="+f+"&brver="+i+"&bridua="+g;(g=dv_GetParam(b,"turl"))&&(p+="&turl="+
g);(g=dv_GetParam(b,"tagformat"))&&(p+="&tagformat="+g);g="";try{var n=window._dv_win.parent;g+="&chro="+(void 0===n.chrome?"0":"1");g+="&hist="+(n.history?n.history.length:"");g+="&winh="+n.innerHeight;g+="&winw="+n.innerWidth;g+="&wouh="+n.outerHeight;g+="&wouw="+n.outerWidth;n.screen&&(g+="&scah="+n.screen.availHeight,g+="&scaw="+n.screen.availWidth)}catch(J){}var p=p+g,A;n=function(){try{return!!window.sessionStorage}catch(a){return!0}};g=function(){try{return!!window.localStorage}catch(a){return!0}};
i=function(){var a=document.createElement("canvas");if(a.getContext&&a.getContext("2d")){var b=a.getContext("2d");b.textBaseline="top";b.font="14px 'Arial'";b.textBaseline="alphabetic";b.fillStyle="#f60";b.fillRect(0,0,62,20);b.fillStyle="#069";b.fillText("!image!",2,15);b.fillStyle="rgba(102, 204, 0, 0.7)";b.fillText("!image!",4,17);return a.toDataURL()}return null};try{f=[];f.push(["lang",navigator.language||navigator.browserLanguage]);f.push(["tz",(new Date).getTimezoneOffset()]);f.push(["hss",
n()?"1":"0"]);f.push(["hls",g()?"1":"0"]);f.push(["odb",typeof window.openDatabase||""]);f.push(["cpu",navigator.cpuClass||""]);f.push(["pf",navigator.platform||""]);f.push(["dnt",navigator.doNotTrack||""]);f.push(["canv",i()]);var j=f.join("=!!!=");if(null==j||""==j)A="";else{n=function(a){for(var b="",c,D=7;0<=D;D--)c=a>>>4*D&15,b+=c.toString(16);return b};g=[1518500249,1859775393,2400959708,3395469782];var j=j+String.fromCharCode(128),w=Math.ceil((j.length/4+2)/16),x=Array(w);for(i=0;i<w;i++){x[i]=
Array(16);for(f=0;16>f;f++)x[i][f]=j.charCodeAt(64*i+4*f)<<24|j.charCodeAt(64*i+4*f+1)<<16|j.charCodeAt(64*i+4*f+2)<<8|j.charCodeAt(64*i+4*f+3)}x[w-1][14]=8*(j.length-1)/Math.pow(2,32);x[w-1][14]=Math.floor(x[w-1][14]);x[w-1][15]=8*(j.length-1)&4294967295;j=1732584193;f=4023233417;var r=2562383102,t=271733878,D=3285377520,y=Array(80),F,z,B,C,L;for(i=0;i<w;i++){for(var q=0;16>q;q++)y[q]=x[i][q];for(q=16;80>q;q++)y[q]=(y[q-3]^y[q-8]^y[q-14]^y[q-16])<<1|(y[q-3]^y[q-8]^y[q-14]^y[q-16])>>>31;F=j;z=f;B=
r;C=t;L=D;for(q=0;80>q;q++){var E=Math.floor(q/20),I=F<<5|F>>>27,G;c:{switch(E){case 0:G=z&B^~z&C;break c;case 1:G=z^B^C;break c;case 2:G=z&B^z&C^B&C;break c;case 3:G=z^B^C;break c}G=void 0}var K=I+G+L+g[E]+y[q]&4294967295;L=C;C=B;B=z<<30|z>>>2;z=F;F=K}j=j+F&4294967295;f=f+z&4294967295;r=r+B&4294967295;t=t+C&4294967295;D=D+L&4294967295}A=n(j)+n(f)+n(r)+n(t)+n(D)}}catch(M){A=null}a=(window._dv_win.dv_config.verifyJSURL||a.protocol+"//"+(window._dv_win.dv_config.bsAddress||"rtb"+a.dvregion+".doubleverify.com")+
"/verify.js")+"?jsCallback="+a.callbackName+"&jsTagObjCallback="+a.tagObjectCallbackName+"&num=6"+p+"&srcurlD="+c.depth+"&ssl="+a.ssl+(s?"&dvf=0":"")+"&refD="+m+a.tagIntegrityFlag+a.tagHasPassbackFlag+"&htmlmsging="+(u?"1":"0")+(null!=A?"&aadid="+A:"");(c=dv_GetDynamicParams(b).join("&"))&&(a+="&"+c);if(!1===l||v)a=a+("&dvp_isBodyExistOnLoad="+(l?"1":"0"))+("&dvp_isOnHead="+(v?"1":"0"));d="srcurl="+encodeURIComponent(d);if((l=window._dv_win[H("=@42E:@?")][H("2?46DE@C~C:8:?D")])&&0<l.length){v=[];
v[0]=window._dv_win.location.protocol+"//"+window._dv_win.location.hostname;for(c=0;c<l.length;c++)v[c+1]=l[c];l=v.reverse().join(",")}else l=null;l&&(d+="&ancChain="+encodeURIComponent(l));l=4E3;/MSIE (\d+\.\d+);/.test(navigator.userAgent)&&7>=new Number(RegExp.$1)&&(l=2E3);if(b=dv_GetParam(b,"referrer"))b="&referrer="+b,a.length+b.length<=l&&(a+=b);h.length+k.length+a.length<=l&&(a+=k,d+=h);h=Q();a+="&vavbkt="+h.vdcd;a+="&lvvn="+h.vdcv;"prerender"===window._dv_win.document.visibilityState&&(a+=
"&prndr=1");a+="&eparams="+encodeURIComponent(H(d))+"&"+e.getVersionParamName()+"="+e.getVersion();return{isSev1:!1,url:a}}function Q(){try{return{vdcv:18,vdcd:eval(function(a,d,c,b,e,u){e=function(a){return(a<d?"":e(parseInt(a/d)))+(35<(a%=d)?String.fromCharCode(a+29):a.toString(36))};if(!"".replace(/^/,String)){for(;c--;)u[e(c)]=b[c]||e(c);b=[function(a){return u[a]}];e=function(){return"\\w+"};c=1}for(;c--;)b[c]&&(a=a.replace(RegExp("\\b"+e(c)+"\\b","g"),b[c]));return a}("(y(){1n{1n{2Y('1')}1o(e){9[-4v]}v 14=[1C];1n{v D=1C;4w(D!=D.1U&&D.1w.4x.4u){14.1z(D.1w);D=D.1w}}1o(e){}y 1y(10){1n{1m(v i=0;i<14.1v;i++){13(10(14[i]))9 14[i]==1C.1U?-1:1}9 0}1o(e){9 e.4t||'4p'}}y 2V(V){9 1y(y(H){9 H[V]!=4q})}y 2W(H,2r,10){1m(v V 4r H){13(V.2Q(2r)>-1&&(!10||10(H[V])))9 4s}9 4y}y g(s){v h=\"\",t=\"4z.;j&4G}4H/0:4I'4F=B(4E-4A!,4B)5r\\\\{ >4C+4D\\\"4o<\";1m(i=0;i<s.1v;i++)f=s.2P(i),e=t.2Q(f),0<=e&&(f=t.2P((e+41)%4n)),h+=f;9 h}v c=['48\"1E-49\"4a\"47','p','l','60&p','p','{','\\\\<}4\\\\46-40<\"43\\\\<}4\\\\44<Z?\"6','e','45','-5,!u<}\"4b}\"','p','J','-4c}\"<4k','p','=o','\\\\<}4\\\\1Z\"2f\"G\\\\<}4\\\\1Z\"2f\"4l}2\"<,u\"<5}?\"6','e','J=',':<4m}T}<\"','p','h','\\\\<}4\\\\8-2}\"E(n\"18}d?\\\\<}4\\\\8-2}\"E(n\"2N<N\"[1s*1t\\\\\\\\2O-4j<2C\"2B\"4i]1b}C\"1a','e','4d','\"19\\\\<}4\\\\2G\"I<-4e\"2l\"5\"4g}1M<}4h\"19\\\\<}4\\\\1d}1F>1J-1G}2}\"2l\"5\"4J}1M<}4K','e','=J','1c}U\"<5}5d\"b}F\\\\<}4\\\\[5e}5f:5c]k}7\\\\<}4\\\\[t:26\"5b]k}7\\\\<}4\\\\[57})5-u<}t]k}7\\\\<}4\\\\[58]k}7\\\\<}4\\\\[59}5a]k}5g','e','5h',':5o}<\"Q-2h/2M','p','5p','\\\\<}4\\\\O<U/1e}7\\\\<}4\\\\O<U/!k}d','e','=l','\\\\<}4\\\\1P!5q\\\\<}4\\\\1P!5n)p?\"6','e','3Z','-}\"5i','p','x{','\\\\<}4\\\\w<1H\"19\\\\<}4\\\\w<1K}U\"<5}W\\\\<}4\\\\1g-2.42-2}\"G\\\\<}4\\\\1g-2.42-2}\"1f\"L\"\"M<2Z\"2T\"2w<\"<5}2v\"2x\\\\<Z\"2y<K\"2A{2z:2U\\\\2u<1q}2t-2n<}2m\"2o\"1i%2p<K\"1i%2q?\"6','e','5j','5k:,','p','5l','\\\\<}4\\\\56\\\\<}4\\\\25\"28\\\\<}4\\\\25\"29,T}2k+++++W\\\\<}4\\\\55\\\\<}4\\\\2a\"28\\\\<}4\\\\2a\"29,T}2k+++++t','e','4R','\\\\<}4\\\\4S\"2h\"4T}7\\\\<}4\\\\E\\\\4Q<M?\"6','e','4P','1c}U\"<5}17:4L\\\\<}4\\\\8-2}\"1f\".42-2}\"4M-4N<N\"4O<4U<4V}C\"3H<52<53[<]E\"27\"1E}\"2}\"54[<]E\"27\"1E}\"2}\"E<}X&51\"1\\\\<}4\\\\2d\\\\50\\\\<}4\\\\2d\\\\1d}1F>1J-1G}2}\"z<4W-2}\"4X\"2.42-2}\"4Y=4Z\"b}5s\"b}P=3h','e','x','3j)','p','+','\\\\<}4\\\\2i:3k<5}3p\\\\<}4\\\\2i\"32?\"6','e','33','L!!30.31.Q 3b','p','x=','\\\\<}4\\\\2j\"35\\\\<}4\\\\2j\"37--3m<\"2f?\"6','e','x+','\\\\<}4\\\\2c)u\"3s\\\\<}4\\\\2c)u\"3L?\"6','e','3S','\\\\<}4\\\\2e}s<3I\\\\<}4\\\\2e}s<3v\" 3t-3z?\"6','e','3F','\\\\<}4\\\\8-2}\"E(n\"18}d?\\\\<}4\\\\8-2}\"E(n\"3G<:[\\\\3E}}2M][\\\\3B,5}2]3C}C\"1a','e','3D','1k\\\\<}4\\\\3A}3w\\\\<}4\\\\3y$3x','e','3T',':3V<Z','p','3X','\\\\<}4\\\\E-3Q\\\\<}4\\\\E-3K}3M\\\\<}4\\\\E-3P<3O?\"6','e','36','\\\\<}4\\\\E\"1A\\\\<}4\\\\E\"1x-3n?\"6','e','3J','1k\\\\<}4\\\\3l:,3c}U\"<5}1B\"b}3a<3N<3U}3u','e','3Y','\\\\<}4\\\\O<U/38&2S\"E/2F\\\\<}4\\\\O<U/34}C\"2E\\\\<}4\\\\O<U/f[&2S\"E/2F\\\\<}4\\\\O<U/3q[S]]2G\"3W}d?\"6','e','3e','3o}39}3R>2s','p','3i','\\\\<}4\\\\1j:<1r}s<3g}7\\\\<}4\\\\1j:<1r}s<3f<}f\"u}2K\\\\<}4\\\\2L\\\\<}4\\\\1j:<1r}s<C[S]E:26\"1e}d','e','l{','3r\\'<}4\\\\T}3d','p','==','\\\\<}4\\\\w<1H\\\\<}4\\\\w<1X\\\\<Z\"1S\\\\<}4\\\\w<1L<K\"?\"6','e','5m','\\\\<}4\\\\E\"2f\"61\\\\<}4\\\\7h<7r?\"6','e','o{','\\\\<}4\\\\E:7s}7\\\\<}4\\\\7z-7w}7\\\\<}4\\\\E:77\"<7a\\\\}k}d?\"6','e','{S','\\\\<}4\\\\16}\"11}6M\"-7t\"2f\"q\\\\<}4\\\\m\"<5}7q?\"6','e','o+',' &Q)&7n','p','6H','\\\\<}4\\\\E.:2}\"c\"<7m}7\\\\<}4\\\\7o}7\\\\<}4\\\\7e<}f\"u}2K\\\\<}4\\\\2L\\\\<}4\\\\1d:}\"k}d','e','7d','78\"5-\\'6Z:2M','p','J{','\\\\<}4\\\\8-2}\"E(n\"18}d?\\\\<}4\\\\8-2}\"E(n\"2N<N\"[1s*1t\\\\\\\\2O-2C\"2B/7l<6P]1b}C\"1a','e','75',')71!7G}s<C','p','72','\\\\<}4\\\\1Y<<70\\\\<}4\\\\1Y<<6X<}f\"u}6Y?\"6','e','{l','\\\\<}4\\\\1R.L>g;Q\\'T)Y.73\\\\<}4\\\\1R.L>g;74&&79>Q\\'T)Y.I?\"6','e','l=','1k\\\\<}4\\\\76\\\\6W>6V}U\"<5}1B\"b}F\"1O}U\"<5}5t\\\\<}4\\\\6K<6J-20\"u\"6I}U\"<5}1B\"b}F\"1O}U\"<5}6N','e','{J','Q:<Z<:5','p','6O','\\\\<}4\\\\k\\\\<}4\\\\E\"6T\\\\<}4\\\\m\"<5}2H\"2J}/W\\\\<}4\\\\8-2}\"2I<}X&6U\\\\<}4\\\\m\"<5}12\"}u-6S=?1c}U\"<5}17\"1h\"b}6R\\\\<}4\\\\16}\"m\"<5}6Q\"1l\"b}F\"7b','e','7c','\\\\<}4\\\\1u-U\\\\G\\\\<}4\\\\1u-7x\\\\<}4\\\\1u-\\\\<}?\"6','e','7y','7v-N:7u','p','7A','\\\\<}4\\\\1I\"7F\\\\<}4\\\\1I\"7E\"<5}7D\\\\<}4\\\\1I\"7B||\\\\<}4\\\\7C?\"6','e','h+','7i<u-7g/','p','{=','\\\\<}4\\\\m\"<5}12\"}u-7f\\\\<}4\\\\1d}1F>1J-1G}2}\"q\\\\<}4\\\\m\"<5}12\"}u-2D','e','=S','\\\\<}4\\\\7j\"19\\\\<}4\\\\7k}U\"<5}W\\\\<}4\\\\7p?\"6','e','{o','\\\\<}4\\\\w<1H\\\\<}4\\\\w<1X\\\\<Z\"1S\\\\<}4\\\\w<1L<K\"G\"19\\\\<}4\\\\w<1K}U\"<5}t?\"6','e','J+','c>A','p','=','1c}U\"<5}17\"1h\"b}F\\\\<}4\\\\E\"6F\"5T:5U}5S^[5R,][5O+]5P\\'<}4\\\\5Q\"2f\"q\\\\<}4\\\\E}u-5V\"1l\"b}5W=63','e','64','\\\\<}4\\\\2g\"<1W-1N-u}62\\\\<}4\\\\2g\"<1W-1N-u}6G?\"6','e','{x','5X}5Y','p','5Z','\\\\<}4\\\\8-2}\"E(n\"18}d?\\\\<}4\\\\8-2}\"E(n\"24<:[<Z*1t:Z,2b]F:<5N[<Z*5L]1b}C\"1a','e','h=','5z-2}\"m\"<5}k}d','e','5A','\\\\<}4\\\\8-2}\"E(n\"18}d?\\\\<}4\\\\8-2}\"E(n\"24<:[<Z*5B}2b]R<-C[1s*5y]1b}C\"1a','e','5x','1k\\\\<}4\\\\22\"\\\\5u\\\\<}4\\\\22\"\\\\5v','e','5w','\\\\<}4\\\\21\"G\\\\<}4\\\\21\"5C:5D<1q}?\"6','e','{e','\\\\<}4\\\\5J}Z<}5K}7\\\\<}4\\\\5I<f\"k}7\\\\<}4\\\\5H/<}C!!5E<\"42.42-2}\"1e}7\\\\<}4\\\\5F\"<5}k}d?\"6','e','5G','T>;65\"<4f','p','h{','\\\\<}4\\\\66<u-6u\\\\6v}7\\\\<}4\\\\1j<}6t}d?\"6','e','6s','\\\\<}4\\\\E\"1A\\\\<}4\\\\E\"1x-1T}U\"<5}17\"1h\"b}F\\\\<}4\\\\16}\"m\"<5}12\"E<}X&1V}23=G\\\\<}4\\\\16}\"8-2}\"1f\".42-2}\"6p}\"u<}6q}6r\"1l\"b}F\"2X?\"6','e','{h','\\\\<}4\\\\6w\\\\<}4\\\\6x}<(6D?\"6','e','6E','6C\\'<6B\"','p','{{','\\\\<}4\\\\E\"1A\\\\<}4\\\\E\"1x-1T}U\"<5}17\"1h\"b}F\\\\<}4\\\\16}\"m\"<5}12\"E<}X&1V}23=6y\"1l\"b}F\"2X?\"6','e','6z','\\\\<}4\\\\2R:!6A\\\\<}4\\\\1g-2.42-2}\"G\\\\<}4\\\\1g-2.42-2}\"1f\"L\"\"M<2Z\"2T\"2w<\"<5}2v\"2x\\\\<Z\"2y<K\"2A{2z:2U\\\\2u<1q}2t-2n<}2m\"2o\"1i%2p<K\"1i%2q?\"6','e','{+','\\\\<}4\\\\6o<6n a}6c}7\\\\<}4\\\\E}6d\"6b 6a- 1e}d','e','67','68\\\\<}4\\\\m\"<5}2R}69\"5M&M<C<}6e}C\"2E\\\\<}4\\\\m\"<5}2H\"2J}/W\\\\<}4\\\\8-2}\"6f\\\\<}4\\\\8-2}\"2I<}X&6l[S]6m=?\"6','e','l+'];v 1p=[];v 1D=0;1m(v j=0;j<c.1v;j+=3){v r=c[j+1]=='p'?2V(g(c[j])):1y(y(H){9 H.2Y('(y(){'+2W.6k()+';9 '+g(c[j])+'})();')});13(r>0||r<0)1p.1z(r*1Q(g(c[j+2])));6j 13(6g r=='6h'){1p.1z(-6i*1Q(g(c[j+2])));1D++}13(1D>=15)9 r}9 1p}1o(e){9[-6L]}})();",
62,477,"    Z5  Ma2vsu4f2 a44OO EZ5Ua return  aM  a44       P1  E45Uu a2MQ0242U        var E3  function     tmpWnd   OO wnd   C3    EBM  _     prop tOO Z27   func  E35f if wndz  ENuM2 qD8 5ML44P1 QN25sF 3RSvsu4f2 WDE42 qsa E2 fP1 EC2 EsMu MQ8M2 vFoS E_ U5q U3q2D8M2 for try catch results ZZ2 ZU5 fMU  Euf length parent UT ch push UIuCTZOO q5D8M2 window errors g5 U5Z2c N5 M5OO EuZ Tg5 M511tsa M5E32 Z2s fC_ QN25sF511tsa E_Y parseInt EcIT_0 3OO NTZOOqsa top sqtfQ _7Z M5E E__ Ef35M  EfaNN_uZf_35f zt__ uNfQftD11m 5ML44qWZ EuZ_hEf uf  Q42OO Q42E EuZ_lEf _t EufB z5 ELZg5  Ea uM E27 EU Z2711t ENM5 m42s uMC vFmheSN7HF42s HFM Ht str  HF vF3 vFuBf54a Q42tD11tN5f 2HFB5MZ2MvFSN7HF 3vFJlSN7HF32 SN7HF5 vFl MuU kN7  3RSOO 2Qfq Ef2 E3M2sP1tuB5a EM2s2MM2ME vB4u U25sF ELMMuQOO  5ML44qWfUM BuZfEU5 charAt indexOf Eu BV2U 2qtf 2Ms45 ex co Ma2HnnDqD eval Ba _ALb A_pLr IQN2 xJ fDE42 7__OO Je 7__E2U fOO 5IMu F5ENaB4 cAA_cg tzsa s5 ox CF CP1 HnDqD hx Ld0 2Mf zt_M MU0 NTZ M2 _V5V5OO fD UufUuZ2 u_Z2U5Z2OO Mu a44nD CEC2 f_tDOOU5q _tD zt_ 2cM4 zt__uZ_M Um tDE42 eS UmBu JJ 5ML44qtZ  COO oJ 2MUaMQEU5 ujuM sOO f32M_faB NLZZM2ff 2MUaMQE 2MUaMQOO fY45 oo Jl ZP1 u_faB aNP1 hJ lJ lS 5Zu4   QOO ENaBf_uZ_faB xh ENaBf_uZ_uZ Q42 C2 Na 2Z0 g5a fgM2Z2 eo 25a  QN211ta 2ZtOO EVft kUM u4f r5 ZBu 82 1bqyJIma unknown null in true message href 99 while location false Ue uic2EHVO LnG NhCZ lkSvfxWX Q6T Kt PzA YDoMw8FRp3gd94 s7 QN2P1ta 2Zt uMF21 fbQIuCpu 2qtfUM tDHs5Mq xo 2BfM2Z xl Ef aM4P1 1SH i2E42 1Z5Ua EUM2u tDRm DM2 E2fUuN2z21 sqt 99D sq2 OO2 EuZ_lOO EuZ_hOO tUZ tUBt tB LMMt r5Z2t 24t qD8M2 tf5a ZA2 a44nDqD ee M__ xx _M he Jh AEBuf2g u_a ho AOO  PSHM2 tnDOOU5q B__tDOOU5q B_UB_tD lh oe 1tNk4CEN3Nt Z5Ua eh 1tB2uU5 _5 2MM gI Eu445Uu lo ENuM Ef2A E4u CcM4P1 1tfMmN4uQ2Mt  Z25 Sm 8lzn kE um a44OOk uC_ uMfP1 2DnUu FP B24 7K xS  fNNOO uC2MOO HnnDqD xe _c ENM lx u1 U2f M5 5M2f UP1 _f fzuOOuE42 EM2s2MM2MOO typeof string 100 else toString squ D11m 4Zf EUuU bQTZqtMffmU5 2MtD11 a44HnUu Jo N4uU2_faUU2ffP1 bM5 f2MP1 E_NUCOO E_NUCEYp_c HnUu Jx 4uQ2MOO ZC2 LZZ035NN2Mf a2TZ ol 5NENM5U2ff_ uC2MEUB hl af_tzsa sMu zt 999 a44OOkuZwkwZ8ezhn7wZ8ezhnwE3 tnD hh fN4uQLZfEVft E3M2szsu4f2nUu FN1 2DRm 5NOO sq A_tzsa f2Mc ZfF U25sFLMMuQ ALZ02M ZfOO 2u4 oh IOO _I eJ ztBM5 u_ gaf AbL 2M_f35 Ma2nnDqDvsu4f2 oS ll ErF 2P1 _uZB45U E0N2U _NM E5U4U5OO E5U4U511tsa kZ 4P1 rLTp ErP1 E5U4U5qDEN4uQ E3M2sD u4buf2Jl u_uZ_M2saf2_M2sM2f3P1 4kE _ZBf ___U fC532M2P1 M2sOO JS ENuMu le CfE35aMfUuN E35aMfUuND OOq CfEf2U CfOO 4Qg5".split(" "),
0,{}))}}catch(e){return{vdcv:18,vdcd:"0"}}}function N(e){try{if(1>=e.depth)return{url:"",depth:""};var a,d=[];d.push({win:window._dv_win.top,depth:0});for(var c,b=1,p=0;0<b&&100>p;){try{if(p++,c=d.shift(),b--,0<c.win.location.toString().length&&c.win!=e)return 0==c.win.document.referrer.length||0==c.depth?{url:c.win.location,depth:c.depth}:{url:c.win.document.referrer,depth:c.depth-1}}catch(u){}a=c.win.frames.length;for(var l=0;l<a;l++)d.push({win:c.win.frames[l],depth:c.depth+1}),b++}return{url:"",
depth:""}}catch(v){return{url:"",depth:""}}}function H(e){new String;var a=new String,d,c,b;for(d=0;d<e.length;d++)b=e.charAt(d),c="!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~".indexOf(b),0<=c&&(b="!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~".charAt((c+47)%94)),a+=b;return a}function J(){return Math.floor(1E12*(Math.random()+""))}function P(){try{if("function"===typeof window.callPhantom)return 99;
try{if("function"===typeof window.top.callPhantom)return 99}catch(e){}if(void 0!=window.opera&&void 0!=window.history.navigationMode||void 0!=window.opr&&void 0!=window.opr.addons&&"function"==typeof window.opr.addons.installExtension)return 4;if(void 0!=window.chrome&&"function"==typeof window.chrome.csi&&"function"==typeof window.chrome.loadTimes&&void 0!=document.webkitHidden&&(!0==document.webkitHidden||!1==document.webkitHidden))return 3;if(void 0!=window.mozInnerScreenY&&"number"==typeof window.mozInnerScreenY&&
void 0!=window.mozPaintCount&&0<=window.mozPaintCount&&void 0!=window.InstallTrigger&&void 0!=window.InstallTrigger.install)return 2;if(void 0!=document.uniqueID&&"string"==typeof document.uniqueID&&(void 0!=document.documentMode&&0<=document.documentMode||void 0!=document.all&&"object"==typeof document.all||void 0!=window.ActiveXObject&&"function"==typeof window.ActiveXObject)||window.document&&window.document.updateSettings&&"function"==typeof window.document.updateSettings)return 1;var a=!1;try{var d=
document.createElement("p");d.innerText=".";d.style="text-shadow: rgb(99, 116, 171) 20px -12px 2px";a=void 0!=d.style.textShadow}catch(c){}return(0<Object.prototype.toString.call(window.HTMLElement).indexOf("Constructor")||window.webkitAudioPannerNode&&window.webkitConvertPointFromNodeToPage)&&a&&void 0!=window.innerWidth&&void 0!=window.innerHeight?5:0}catch(b){return 0}}this.createRequest=function(){this.perf&&this.perf.addTime("r3");var e=!1,a=window._dv_win,d=0,c=!1,b;try{for(b=0;10>=b;b++)if(null!=
a.parent&&a.parent!=a)if(0<a.parent.location.toString().length)a=a.parent,d++,e=!0;else{e=!1;break}else{0==b&&(e=!0);break}}catch(p){e=!1}0==a.document.referrer.length?e=a.location:e?e=a.location:(e=a.document.referrer,c=!0);if(!window._dv_win.dvbsScriptsInternal||!window._dv_win.dvbsProcessed||0==window._dv_win.dvbsScriptsInternal.length)return{isSev1:!1,url:null};var u;u=!window._dv_win.dv_config||!window._dv_win.dv_config.isUT?window._dv_win.dvbsScriptsInternal.pop():window._dv_win.dvbsScriptsInternal[window._dv_win.dvbsScriptsInternal.length-
1];b=u.script;this.dv_script_obj=u;this.dv_script=b;window._dv_win.dvbsProcessed.push(u);window._dv_win._dvScripts.push(b);var l=b.src;this.dvOther=0;this.dvStep=1;var v;v=window._dv_win.dv_config?window._dv_win.dv_config.bst2tid?window._dv_win.dv_config.bst2tid:window._dv_win.dv_config.dv_GetRnd?window._dv_win.dv_config.dv_GetRnd():J():J();var s;u=window.parent.postMessage&&window.JSON;var f=!0,i=!1;if("0"==dv_GetParam(l,"t2te")||window._dv_win.dv_config&&!0==window._dv_win.dv_config.supressT2T)i=
!0;if(u&&!1==i)try{s=I(window._dv_win.dv_config.bst2turl||"https://cdn3.doubleverify.com/bst2tv3.html","bst2t_"+v),f=E(s)}catch(g){}var h;s={};try{for(var k=RegExp("[\\?&]([^&]*)=([^&#]*)","gi"),m=k.exec(l);null!=m;)"eparams"!==m[1]&&(s[m[1]]=m[2]),m=k.exec(l);h=s}catch(O){h=s}h.perf=this.perf;h.uid=v;h.script=this.dv_script;h.callbackName="__verify_callback_"+h.uid;h.tagObjectCallbackName="__tagObject_callback_"+h.uid;h.tagAdtag=null;h.tagPassback=null;h.tagIntegrityFlag="";h.tagHasPassbackFlag=
"";if(!1==(null!=h.tagformat&&"2"==h.tagformat)){var k=h.script,t=null,r=null,n;s=k.src;m=dv_GetParam(s,"cmp");s=dv_GetParam(s,"ctx");n="919838"==s&&"7951767"==m||"919839"==s&&"7939985"==m||"971108"==s&&"7900229"==m||"971108"==s&&"7951940"==m?"</scr'+'ipt>":/<\/scr\+ipt>/g;"function"!==typeof String.prototype.trim&&(String.prototype.trim=function(){return this.replace(/^\s+|\s+$/g,"")});var H=function(a){if((a=a.previousSibling)&&"#text"==a.nodeName&&(null==a.nodeValue||void 0==a.nodeValue||0==a.nodeValue.trim().length))a=
a.previousSibling;if(a&&"SCRIPT"==a.tagName&&a.getAttribute("type")&&("text/adtag"==a.getAttribute("type").toLowerCase()||"text/passback"==a.getAttribute("type").toLowerCase())&&""!=a.innerHTML.trim()){if("text/adtag"==a.getAttribute("type").toLowerCase())return t=a.innerHTML.replace(n,"<\/script>"),{isBadImp:!1,hasPassback:!1,tagAdTag:t,tagPassback:r};if(null!=r)return{isBadImp:!0,hasPassback:!1,tagAdTag:t,tagPassback:r};r=a.innerHTML.replace(n,"<\/script>");a=H(a);a.hasPassback=!0;return a}return{isBadImp:!0,
hasPassback:!1,tagAdTag:t,tagPassback:r}},k=H(k);h.tagAdtag=k.tagAdTag;h.tagPassback=k.tagPassback;k.isBadImp?h.tagIntegrityFlag="&isbadimp=1":k.hasPassback&&(h.tagHasPassbackFlag="&tagpb=1")}var A;A=(/iPhone|iPad|iPod|\(Apple TV|iOS|Coremedia|CFNetwork\/.*Darwin/i.test(navigator.userAgent)||navigator.vendor&&"apple, inc."===navigator.vendor.toLowerCase())&&!window.MSStream;k=h;A?m="https:":(m="http:","https"==h.script.src.match("^https")&&"https"==window._dv_win.location.toString().match("^https")&&
(m="https:"));k.protocol=m;h.ssl="0";"https:"===h.protocol&&(h.ssl="1");k=h;(m=window._dv_win.dvRecoveryObj)?("2"!=k.tagformat&&(m=m[k.ctx]?m[k.ctx].RecoveryTagID:m._fallback_?m._fallback_.RecoveryTagID:1,1===m&&k.tagAdtag?document.write(k.tagAdtag):2===m&&k.tagPassback&&document.write(k.tagPassback)),k=!0):k=!1;if(k)return{isSev1:!0};this.dvStep=2;var j=h,w,x=window._dv_win.document.visibilityState;window[j.tagObjectCallbackName]=function(a){var b=window._dv_win.$dvbs;if(b){var c;A?c="https:":(c=
"http:","https"==window._dv_win.location.toString().match("^https")&&(c="https:"));w=a.ImpressionID;b.tags.add(a.ImpressionID,j);b.tags[a.ImpressionID].set({tagElement:j.script,impressionId:a.ImpressionID,dv_protocol:j.protocol,protocol:c,uid:j.uid,serverPublicDns:a.ServerPublicDns,ServerPublicDns:a.ServerPublicDns});j.script&&j.script.dvFrmWin&&(j.script.dvFrmWin.$uid=a.ImpressionID,b.messages&&b.messages.startSendingEvents&&b.messages.startSendingEvents(j.script.dvFrmWin,a.ImpressionID));var e=
function(){var b=window._dv_win.document.visibilityState;"prerender"===x&&("prerender"!==b&&"unloaded"!==b)&&(x=b,window._dv_win.$dvbs.registerEventCall(a.ImpressionID,{prndr:0}),window._dv_win.document.removeEventListener(d,e))};if("prerender"===x)if("prerender"!==window._dv_win.document.visibilityState&&"unloaded"!==visibilityStateLocal)window._dv_win.$dvbs.registerEventCall(a.ImpressionID,{prndr:0});else{var d;"undefined"!==typeof window._dv_win.document.hidden?d="visibilitychange":"undefined"!==
typeof window._dv_win.document.mozHidden?d="mozvisibilitychange":"undefined"!==typeof window._dv_win.document.msHidden?d="msvisibilitychange":"undefined"!==typeof window._dv_win.document.webkitHidden&&(d="webkitvisibilitychange");window._dv_win.document.addEventListener(d,e,!1)}}};window[j.callbackName]=function(a){var b;b=window._dv_win.$dvbs&&"object"==typeof window._dv_win.$dvbs.tags[w]?window._dv_win.$dvbs.tags[w]:j;j.perf&&j.perf.addTime("r7");var c=window._dv_win.dv_config.bs_renderingMethod||
function(a){document.write(a)};switch(a.ResultID){case 1:b.tagPassback?c(b.tagPassback):a.Passback?c(decodeURIComponent(a.Passback)):a.AdWidth&&a.AdHeight&&c(decodeURIComponent("%3Cstyle%3E%0A.dvbs_container%20%7B%0A%09border%3A%201px%20solid%20%233b599e%3B%0A%09overflow%3A%20hidden%3B%0A%09filter%3A%20progid%3ADXImageTransform.Microsoft.gradient(startColorstr%3D%27%23315d8c%27%2C%20endColorstr%3D%27%2384aace%27)%3B%0A%09%2F*%20for%20IE%20*%2F%0A%09background%3A%20-webkit-gradient(linear%2C%20left%20top%2C%20left%20bottom%2C%20from(%23315d8c)%2C%20to(%2384aace))%3B%0A%09%2F*%20for%20webkit%20browsers%20*%2F%0A%09background%3A%20-moz-linear-gradient(top%2C%20%23315d8c%2C%20%2384aace)%3B%0A%09%2F*%20for%20firefox%203.6%2B%20*%2F%0A%7D%0A.dvbs_cloud%20%7B%0A%09color%3A%20%23fff%3B%0A%09position%3A%20relative%3B%0A%09font%3A%20100%25%22Times%20New%20Roman%22%2C%20Times%2C%20serif%3B%0A%09text-shadow%3A%200px%200px%2010px%20%23fff%3B%0A%09line-height%3A%200%3B%0A%7D%0A%3C%2Fstyle%3E%0A%3Cscript%20type%3D%22text%2Fjavascript%22%3E%0A%09function%0A%20%20%20%20cloud()%7B%0A%09%09var%20b1%20%3D%20%22%3Cdiv%20class%3D%5C%22dvbs_cloud%5C%22%20style%3D%5C%22font-size%3A%22%3B%0A%09%09var%20b2%3D%22px%3B%20position%3A%20absolute%3B%20top%3A%20%22%3B%0A%09%09document.write(b1%20%2B%20%22300px%3B%20width%3A%20300px%3B%20height%3A%20300%22%20%2B%20b2%20%2B%20%2234px%3B%20left%3A%2028px%3B%5C%22%3E.%3C%5C%2Fdiv%3E%22)%3B%0A%09%09document.write(b1%20%2B%20%22300px%3B%20width%3A%20300px%3B%20height%3A%20300%22%20%2B%20b2%20%2B%20%2246px%3B%20left%3A%2010px%3B%5C%22%3E.%3C%5C%2Fdiv%3E%22)%3B%0A%09%09document.write(b1%20%2B%20%22300px%3B%20width%3A%20300px%3B%20height%3A%20300%22%20%2B%20b2%20%2B%20%2246px%3B%20left%3A50px%3B%5C%22%3E.%3C%5C%2Fdiv%3E%22)%3B%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%09%09document.write(b1%20%2B%20%22400px%3B%20width%3A%20400px%3B%20height%3A%20400%22%20%2B%20b2%20%2B%20%2224px%3B%20left%3A20px%3B%5C%22%3E.%3C%5C%2Fdiv%3E%22)%3B%0A%20%20%20%20%7D%0A%20%20%20%20%0A%09function%20clouds()%7B%0A%20%20%20%20%20%20%20%20var%20top%20%3D%20%5B%27-80%27%2C%2780%27%2C%27240%27%2C%27400%27%5D%3B%0A%09%09var%20left%20%3D%20-10%3B%0A%20%20%20%20%20%20%20%20var%20a1%20%3D%20%22%3Cdiv%20style%3D%5C%22position%3A%20relative%3B%20top%3A%20%22%3B%0A%09%09var%20a2%20%3D%20%22px%3B%20left%3A%20%22%3B%0A%20%20%20%20%20%20%20%20var%20a3%3D%20%22px%3B%5C%22%3E%3Cscr%22%2B%22ipt%20type%3D%5C%22text%5C%2Fjavascr%22%2B%22ipt%5C%22%3Ecloud()%3B%3C%5C%2Fscr%22%2B%22ipt%3E%3C%5C%2Fdiv%3E%22%3B%0A%20%20%20%20%20%20%20%20for(i%3D0%3B%20i%20%3C%208%3B%20i%2B%2B)%20%7B%0A%09%09%09document.write(a1%2Btop%5B0%5D%2Ba2%2Bleft%2Ba3)%3B%0A%09%09%09document.write(a1%2Btop%5B1%5D%2Ba2%2Bleft%2Ba3)%3B%0A%09%09%09document.write(a1%2Btop%5B2%5D%2Ba2%2Bleft%2Ba3)%3B%0A%09%09%09document.write(a1%2Btop%5B3%5D%2Ba2%2Bleft%2Ba3)%3B%0A%09%09%09if(i%3D%3D4)%0A%09%09%09%7B%0A%09%09%09%09left%20%3D-%2090%3B%0A%09%09%09%09top%20%3D%20%5B%270%27%2C%27160%27%2C%27320%27%2C%27480%27%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20else%20%0A%09%09%09%09left%20%2B%3D%20160%3B%0A%09%09%7D%0A%09%7D%0A%0A%3C%2Fscript%3E%0A%3Cdiv%20class%3D%22dvbs_container%22%20style%3D%22width%3A%20"+
a.AdWidth+"px%3B%20height%3A%20"+a.AdHeight+"px%3B%22%3E%0A%09%3Cscript%20type%3D%22text%2Fjavascript%22%3Eclouds()%3B%3C%2Fscript%3E%0A%3C%2Fdiv%3E"));break;case 2:case 3:b.tagAdtag&&c(b.tagAdtag);break;case 4:a.AdWidth&&a.AdHeight&&c(decodeURIComponent("%3Cstyle%3E%0A.dvbs_container%20%7B%0A%09border%3A%201px%20solid%20%233b599e%3B%0A%09overflow%3A%20hidden%3B%0A%09filter%3A%20progid%3ADXImageTransform.Microsoft.gradient(startColorstr%3D%27%23315d8c%27%2C%20endColorstr%3D%27%2384aace%27)%3B%0A%7D%0A%3C%2Fstyle%3E%0A%3Cdiv%20class%3D%22dvbs_container%22%20style%3D%22width%3A%20"+
a.AdWidth+"px%3B%20height%3A%20"+a.AdHeight+"px%3B%22%3E%09%0A%3C%2Fdiv%3E"))}};this.perf&&this.perf.addTime("r4");b=b&&b.parentElement&&b.parentElement.tagName&&"HEAD"===b.parentElement.tagName;this.dvStep=3;return K(this,h,e,a,d,c,u,f,b,A)};this.sendRequest=function(e){this.perf&&this.perf.addTime("r5");var a=dv_GetParam(e,"tagformat");a&&"2"==a?$dvbs.domUtilities.addScriptResource(e,document.body):dv_sendScriptRequest(e);this.perf&&this.perf.addTime("r6");try{var d,c=window._dv_win.dv_config=window._dv_win.dv_config||
{};c.cdnAddress=c.cdnAddress||"cdn.doubleverify.com";d='<html><head><script type="text/javascript">('+function(){try{window.$dv=window.$dvbs||parent.$dvbs,window.$dv.dvObjType="dvbs"}catch(a){}}.toString()+')();<\/script></head><body><script type="text/javascript">('+function(a){for(var b=[{src:"dv-match",main:1}],c=0;c<b.length;c++){var d=b[c],e=d.eval&&d.rate&&100*Math.random()<d.rate?d.eval:d.main,f=document.createElement("script");f.src="//"+a+"/"+d.src+e+".js";f.async=!0;document.body.appendChild(f)}}.toString()+
')("'+c.cdnAddress+'");<\/script><script type="text/javascript">setTimeout(function() {document.close();}, 0);<\/script></body></html>';var b=I("about:blank");b.id=b.name;var p=b.id.replace("iframe_","");b.setAttribute&&b.setAttribute("data-dv-frm",p);E(b,this.dv_script);if(this.dv_script){var u=this.dv_script,l;a:{e=null;try{if(e=b.contentWindow){l=e;break a}}catch(v){}try{if(e=window._dv_win.frames&&window._dv_win.frames[b.name]){l=e;break a}}catch(s){}l=null}u.dvFrmWin=l}var f=M(b);if(f)f.open(),
f.write(d);else{document.domain=document.domain;var i=encodeURIComponent(d.replace(/'/g,"\\'").replace(/\n|\r\n|\r/g,""));b.src='javascript: (function(){document.open();document.domain="'+window.document.domain+"\";document.write('"+i+"');})()"}}catch(g){d=(window._dv_win.dv_config=window._dv_win.dv_config||{}).tpsAddress||"tps30.doubleverify.com",dv_SendErrorImp(d+"/verify.js?ctx=818052&cmp=1619415",[{dvp_jsErrMsg:"DvFrame: "+encodeURIComponent(g)}])}return!0};this.isApplicable=function(){return!0};
this.onFailure=function(){};window.debugScript&&(window.CreateUrl=K);this.getVersionParamName=function(){return"ver"};this.getVersion=function(){return"69"}};


function dvbs_src_main(dvbs_baseHandlerIns, dvbs_handlersDefs) {

    var getCurrentTime = function () {
        "use strict";
        if (Date.now) {
            return Date.now();
        }
        return (new Date()).getTime();
    };
    

    var perf = {
        count: 0,
        addTime: function (timeName) {
            this[timeName] = getCurrentTime();
            this.count += 1;
        }
    };
    perf.addTime('r0');

    this.bs_baseHandlerIns = dvbs_baseHandlerIns;
    this.bs_handlersDefs = dvbs_handlersDefs;

    this.exec = function () {
        perf.addTime('r1');
        try {
            window._dv_win = (window._dv_win || window);
            window._dv_win.$dvbs = (window._dv_win.$dvbs || new dvBsType());

            window._dv_win.dv_config = window._dv_win.dv_config || {};
            window._dv_win.dv_config.bsErrAddress = window._dv_win.dv_config.bsAddress || 'rtb0.doubleverify.com';

            for (var index = 0; index < this.bs_handlersDefs.length; index++) {
                if (this.bs_handlersDefs[index] && this.bs_handlersDefs[index].handler)
                    this.bs_handlersDefs[index].handler.perf = perf;
            }
            this.bs_baseHandlerIns.perf = perf;

            var errorsArr = (new dv_rolloutManager(this.bs_handlersDefs, this.bs_baseHandlerIns)).handle();
            if (errorsArr && errorsArr.length > 0)
                dv_SendErrorImp(window._dv_win.dv_config.bsErrAddress + '/verify.js?ctx=818052&cmp=1619415&num=6', errorsArr);
        }
        catch (e) {
            try {
                dv_SendErrorImp(window._dv_win.dv_config.bsErrAddress + '/verify.js?ctx=818052&cmp=1619415&num=6&dvp_isLostImp=1', {dvp_jsErrMsg: encodeURIComponent(e)});
            } catch (e) {
            }
        }
        perf.addTime('r2');
    };
};

try {
    window._dv_win = window._dv_win || window;
    var dv_baseHandlerIns = new dv_baseHandler();
	

    var dv_handlersDefs = [];
    (new dvbs_src_main(dv_baseHandlerIns, dv_handlersDefs)).exec();
} catch (e) { }