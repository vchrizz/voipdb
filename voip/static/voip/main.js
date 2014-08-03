function verifyForm(theForm) {
	if (document.update_nodes_form || document.insert_nodes_form) {
		if (theForm.name.value == '' || !isValidDomainLabel(theForm.name.value)) {
			return formError('Name', 'mag76 (LOWERCASE!) = Margaretenguertel 76\nMaximal 25 Zeichen', theForm.name);
		}
		if (theForm.gps_lat_deg.value != '' || theForm.gps_lat_min.value != '' || theForm.gps_lat_sec.value != '' || theForm.gps_lon_deg.value != '' || theForm.gps_lon_min.value != '' || theForm.gps_lon_sec.value) {
			if (theForm.gps_lat_deg.value < 0 || theForm.gps_lat_deg.value > 90) {
				return formError('GPS Latitude Grad', '48', theForm.gps_lat_deg);
			} else if (theForm.gps_lat_min.value < 0 || theForm.gps_lat_min.value > 59) {
				return formError('GPS Latitude Minuten', '16', theForm.gps_lat_deg);
			} else if (theForm.gps_lat_sec.value < 0 || theForm.gps_lat_sec.value > 59.999) {
				return formError('GPS Latitude Sekunden', '12.345', theForm.gps_lat_sec);
			} else if (theForm.gps_lon_deg.value < 0 || theForm.gps_lon_deg.value > 180) {
				return formError('GPS Longitude Grad', '48', theForm.gps_lon_deg);
			} else if (theForm.gps_lon_min.value < 0 || theForm.gps_lon_min.value > 59) {
				return formError('GPS Longitude Minuten', '16', theForm.gps_lon_deg);
			} else if (theForm.gps_lon_sec.value < 0 || theForm.gps_lon_sec.value > 59.999) {
				return formError('GPS Longitude Sekunden', '12.345', theForm.gps_lon_sec);
			}
		}
	} else if (document.update_devices_form || document.insert_devices_form) {
		if (theForm.name.value == '' || !isValidDomainLabel(theForm.name.value)) {
			return formError('Name', 'mag76omni (LOWERCASE!) = Margaretenguertel 76 Rundstrahler', theForm.name);
		}
	} else if (document.update_member_form || document.insert_member_form) {
		if (document.insert_member_form) {
			if (!doRegexpMatch(/[a-z0-9]{1,25}/gi, theForm.nickname.value)) {
				return formError('Nickname', 'foobar\nMaximal 25 Zeichen', theForm.nickname);
			}
			if (typeof theForm.password != 'undefined')
				 if (theForm.password.value == '' || theForm.password2.value == '' || theForm.password.value != theForm.password2.value) {
					return formError('Passwort', '', theForm.password);
				}
			if (!doRegexpMatch(/[a-z]{1,25}/gi, theForm.firstname.value)) {
				return formError('Vorname', 'Max', theForm.firstname);
			}
			if (theForm.firstname.value.length > 25) {
				return formError('Vorname', 'Max\nMaximal 25 Zeichen', theForm.firstname);
			}
			if (!doRegexpMatch(/[a-z]{1,25}/gi, theForm.lastname.value)) {
				return formError('Nachname', 'Mustermann', theForm.lastname);
			}
			if (theForm.lastname.value.length > 25) {
				return formError('Nachname', 'Mustermann\nMaximal 25 Zeichen', theForm.lastname);
			}
		} else {
			if (theForm.password.value != '') {
				if (theForm.password.value == '' || theForm.password2.value == '' || theForm.password.value != theForm.password2.value) {
					return formError('Passwort', '', theForm.password);
				}
			}
		}
		if (theForm.street.value == '') {
			return formError('Strasse', 'Favoritenstrasse', theForm.street);
		}
		if (theForm.street.value.length > 100) {
			return formError('Strasse', 'Favoritenstrasse\nMaximal 100 Zeichen', theForm.street);
		}
		if (!doRegexpMatch(/([0-9]{1,3}[a-z\-]{0,1}[0-9]{0,3}[0-9 \/.\-]{0,9}[a-z0-9]{0,6})/gi, theForm.housenumber.value) || theForm.housenumber.value.length > 20 ) {
			return formError('Hausnummer', '123a\noder 110-112/3/21', theForm.housenumber);
		}
		if (!doRegexpMatch(/([A-Z\-]{0,3}[0-9A-Z\ ]{4,7})/g, theForm.zip.value)) {
			return formError('PLZ', '1010\noder NL-1234 AB', theForm.zip);
		}
		if (theForm.town.value == '' ) {
			return formError('Ort', 'Wien', theForm.town);
		}
		if (theForm.town.value.length > 100) {
			return formError('Ort', 'Wien\nMaximal 100 Zeichen', theForm.town);
		}
		if (theForm.telephone.value != '' && !doRegexpMatch(/[0-9 +\/-]{1,25}/g, theForm.telephone.value)) {
			return formError('Telefon', '0123456789', theForm.telephone);
		}
		if (theForm.mobilephone.value != '' && !doRegexpMatch(/[0-9 +\/-]{1,25}/g, theForm.mobilephone.value)) {
			return formError('Mobiltelefon', '+43654 1234567', theForm.mobilephone);
		}
		if (theForm.fax.value != '' && !doRegexpMatch(/[0-9 +\/-]{1,25}/g, theForm.fax.value)) {
			return formError('Fax', '0123456789', theForm.fax);
		}
		if (!isValidEmail(theForm.email.value)) {
			return formError('E-Mail', 'admin@funkfeuer.at', theForm.email);
		}
		if (theForm.email.value.length > 50) {
			return formError('E-Mail', 'admin@funkfeuer.at\nMaximal 50 Zeichen', theForm.email);
		}
		if (theForm.homepage.value != '' && !doRegexpMatch(/(http:\/\/.{1,})/g, theForm.homepage.value)) {
			return formError('Homepage', 'http://www.funkfeuer.at/', theForm.homepage);
		}
	} else if (document.update_voip_form || document.insert_voip_form) {
		if (theForm.voicemail.checked) {
			if (theForm.voicemail_pin.value == '' || !doRegexpMatch(/[0-9]{1,4}/g, theForm.voicemail_pin.value)) {
				return formError('Voicemail PIN', '1234', theForm.voicemail_pin);
			}
			if (theForm.voicemail_delay.value == '' || theForm.voicemail_delay.value < 5) {
				return formError('Voicemail Delay', '>= 5', theForm.voicemail_delay);
			}
		}
		if (theForm.h323.checked) {
			if (theForm.h323_ip.value == '') {
				return formError('H323 IP', '123.123.123.123', theForm.h323_ip);
			}
		} else {
			if (theForm.h323_ip.value != '') {
				return formError('H323 IP', 'Leer lassen!', theForm.h323_ip);
			}
		}
	} else if (document.update_voip_sip_form || document.insert_voip_sip_form) {
		if (theForm.secret.value == '' || !doRegexpMatch(/[A-Za-z0-9]{4,16}/g, theForm.secret.value)) {
			return formError('Secret', 'abc1234 (4-16 Stellen)', theForm.secret);
		}
		if (theForm.port.value != '' && !doRegexpMatch(/[0-9]{1,6}/g, theForm.port.value)) {
			return formError('Port', '1234', theForm.port);
		}
		if (theForm.provider.checked) {
			return formError('Provider', 'Wird dzt. nicht supported', theForm.provider);;
			/*
			if (theForm.provider_host.value == '' || theForm.provider_fromuser.value == '' || theForm.provider_fromdomain.value == '' || theForm.provider_secret.value == '') {
				return formError('Provider', 'Alle Provider bezogenen Felder sind verpflichtend', theForm.provider);
			}
			*/
		}
	} else if (document.update_meetme_form || document.insert_meetme_form) {
		if (theForm.meetme_pin.value != '') {
			if (theForm.meetme_pin.value != '' && !doRegexpMatch(/[0-9]{1,4}/g, theForm.meetme_pin.value)) {
				return formError('PIN', '1234', theForm.meetme_pin);
			}
			if (theForm.meetme_admin_pin.value != '' && !doRegexpMatch(/[0-9]{1,4}/g, theForm.meetme_admin_pin.value)) {
				return formError('Admin PIN', '1234', theForm.meetme_admin_pin);
			}
		}
	}
	return true;
}

function formError(errorField, errorExample, errorElement) {
	if (errorExample != '') {
		alert("Eingabefehler bei "+errorField+"\n"+'Beispiel: '+errorExample);
	} else {
		alert("Eingabefehler bei "+errorField);
	}
	errorElement.focus();
	errorElement.select();
	return false;
}

function doRegexpMatch(theRegexp, theValue) {
	if (theValue.match(theRegexp) == theValue) {
		return true;
	} else {
		return false;
	}
}

function isValidEmail(str) {
	return (str.indexOf(".") > 0) && (str.indexOf("@") > 0);
}

function isValidDomainLabel(str) {
	return doRegexpMatch(/[a-z0-9]([a-z0-9\-]{0,23}[a-z0-9])?/ig, str);
}

function isValidMacAddress(str) {
	return doRegexpMatch(/([0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2})/gi, str);
}

function askDelete() {
	return confirm('Wirklich loeschen?');
}

function askResign() {
	return confirm('Wirklich Tech-Contact Zuordnung loeschen?');
}
