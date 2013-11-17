function AndyCampLocation () {
	var divMapa=document.getElementById('map-container');
	var divCoordenadas=document.getElementById('map-support');
	if(navigator.geolocation){
		navigator.geolocation.getCurrentPosition(function(objPosicion){
			var iLatitud=-17.400165696595916;
			var iLongitud=-66.16574585437775;
			var objCoordenadas=new google.maps.LatLng(iLatitud,iLongitud);
			var objOpciones={
				mapTypeId:		google.maps.MapTypeId.ROADMAP,
				zoom: 			16,
				mapTypeControl:	true,
				center: 		objCoordenadas
			};
			var objMapa=new google.maps.Map(divMapa,objOpciones);
			var objPunto=new google.maps.Marker({
				title:		'Android Camp 2013',
				position:	objCoordenadas,
				map:		objMapa,
				icon: "/static/img/marker.png"
			});
		},function(objError){

			switch(objError.code){
				case objError.POSITION_UNAVAILABLE:
					divMapa.innerHTML='<iframe clas="nojs-map" frameborder="0" height="100%" width="100%" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?t=m&amp;hl=es-ES&amp;mapclient=apiv3&amp;ie=UTF8&amp;ll=-17.398825,-66.164346&amp;spn=0.017323,0.033023&amp;z=16&amp;iwloc=lyrftr:m,14846453466306578245,-17.400115,-66.165805&amp;output=embed"></iframe><br/><small><a href="https://maps.google.com/maps?t=m&amp;hl=es-ES&amp;mapclient=apiv3&amp;ie=UTF8&amp;ll=-17.398825,-66.164346&amp;spn=0.017323,0.033023&amp;z=16&amp;iwloc=lyrftr:m,14846453466306578245,-17.400115,-66.165805&amp;source=embed" style="color:#0000FF;text-align:left">Ver mapa más grande</a></small>';
				break;
				case objError.TIMEOUT:
					divMapa.innerHTML='Tiempo de espera agotado.';
				break;
				case objError.PERMISSION_DENIED:
					divMapa.innerHTML='<iframe clas="nojs-map" frameborder="0" height="100%" width="100%" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?t=m&amp;hl=es-ES&amp;mapclient=apiv3&amp;ie=UTF8&amp;ll=-17.398825,-66.164346&amp;spn=0.017323,0.033023&amp;z=16&amp;iwloc=lyrftr:m,14846453466306578245,-17.400115,-66.165805&amp;output=embed"></iframe><br/><small><a href="https://maps.google.com/maps?t=m&amp;hl=es-ES&amp;mapclient=apiv3&amp;ie=UTF8&amp;ll=-17.398825,-66.164346&amp;spn=0.017323,0.033023&amp;z=16&amp;iwloc=lyrftr:m,14846453466306578245,-17.400115,-66.165805&amp;source=embed" style="color:#0000FF;text-align:left">Ver mapa más grande</a></small>';
				break;
				case objError.UNKNOWN_ERROR:
					divMapa.innerHTML='<img src="/static/img/map.png" class="nojs-map"/>';
				break;
			}
		});
	}else{
		divCoordenadas.innerHTML="<img src='/static/img/map.png' class='nojs-map'/>";
	}
}