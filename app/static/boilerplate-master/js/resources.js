game.resources = [
	/**
	 * Graphics.
	 */
	// our level tileset
	{name: "area01_level_tiles",  type:"image",	src: "../static/boilerplate-master/data/img/map/area01_level_tiles.png"},
	// the main player spritesheet
	{name: "gripe_run_right",     type:"image",	src: "../static/boilerplate-master/data/img/sprite/gripe_run_right.png"},
	// the parallax background
	{name: "area01_bkg0",         type:"image",	src: "../static/boilerplate-master/data/img/area01_bkg0.png"},
	{name: "area01_bkg1",         type:"image",	src: "../static/boilerplate-master/data/img/area01_bkg1.png"},
	// the spinning coin spritesheet
	{name: "spinning_coin_gold",  type:"image",	src: "../static/boilerplate-master/data/img/sprite/spinning_coin_gold.png"},
	// our enemty entity
	{name: "wheelie_right",       type:"image",	src: "../static/boilerplate-master/data/img/sprite/wheelie_right.png"},
	// game font
	{name: "32x32_font",          type:"image",	src: "../static/boilerplate-master/data/img/font/32x32_font.png"},
	
	/* 
	 * Maps. 
 	 */
	{name: "area01",              type: "tmx",	src: "../static/boilerplate-master/data/map/area01.tmx"},


	/* 
	 * Background music. 
	 */	
	{name: "dst-inertexponent", type: "audio", src: "../static/boilerplate-master/data/bgm/"},
	
	/* 
	 * Sound effects. 
	 */
	{name: "cling", type: "audio", src: "../static/boilerplate-master/data/sfx/"},
	{name: "stomp", type: "audio", src: "../static/boilerplate-master/data/sfx/"},
	{name: "jump",  type: "audio", src: "../static/boilerplate-master/data/sfx/"}

];