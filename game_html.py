request_game = """<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="utf-8" />
	<link rel="icon" href="https://gttx.app/favicon.png" />
	<!-- <link rel="stylesheet" href={$lib/style/main.css}> -->
	<meta name="viewport" content="width=device-width" />
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<meta http-equiv="content-security-policy" content="">
		<link rel="modulepreload" href="https://gttx.app/_app/immutable/start-8f8d17bc.js">
		<link rel="modulepreload" href="https://gttx.app/_app/immutable/chunks/index-effa2c47.js">
		<link rel="modulepreload" href="https://gttx.app/_app/immutable/chunks/singletons-8688bc0f.js">
		<link rel="modulepreload" href="https://gttx.app/_app/immutable/chunks/index-60d8a1c8.js">
		<link rel="modulepreload" href="https://gttx.app/_app/immutable/chunks/preload-helper-41c905a7.js">
		<link rel="modulepreload" href="https://gttx.app/_app/immutable/components/pages/_layout.svelte-eb36b3f3.js">
		<link rel="modulepreload" href="https://gttx.app/_app/immutable/chunks/pocketbase-6b8fcb7c.js">
		<link rel="modulepreload" href="https://gttx.app/_app/immutable/modules/pages/_layout.ts-9cbb603b.js">
		<link rel="modulepreload" href="https://gttx.app/_app/immutable/chunks/_layout-da46b06b.js">
		<link rel="modulepreload" href="https://gttx.app/_app/immutable/components/pages/(www)/about/_page.svelte-809072ee.js">
</head>

<body data-sveltekit-preload-data="hover">
	<main class="container">
		<div style="display: contents">


<nav><ul><li><a href="https://gttx.app/"><img class="gttx-logo" src="https://gttx.app/svg/gttx_white.svg" alt="gttx!"></a></li></ul>
    <ul><li><a href="https://gttx.app/about">About</a></li>
        <li><a href="https://gttx.app/login">foobar</a></li>
        <li><a href="https://gttx.app/login" role="button">Login</a></li></ul></nav>

<hgroup><h1>Tabletop Exercise</h1>
    <h2 id="TITLE"></h2>
    <h3 id="DESCR"></h3>
<img src="https://www.latech.edu/wp-content/uploads/connections-images/miguel-gates/DJC8822-317e7d64a897dfb4cd7e65a48c181cdd.jpg" alt="hello">


		<script>

            const game_json = %GAMEJSON%;
            document.getElementById("TITLE").innerHTML = game_json.name;
            document.getElementById("DESCR").innerHTML = game_json.description;

		</script>
	</div>
	</main>
</body>

</html>

<style>
	@import url("https://unpkg.com/@picocss/pico@latest/css/pico.min.css");
	@import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;900');
	/* @import url("https://www.unpkg.com/browse/bootstrap-icons@1.10.3/bootstrap-icons.css"); */

	.gttx-logo {
		margin-bottom: 1%;
		opacity: 95%;
		transition: opacity 0.2s;
	}

	.gttx-logo:hover {
		opacity: 100%;
		transition: opacity 0.2s;
	}

	.page-name-header {
		margin-bottom: calc(var(--typography-spacing-vertical) / 3) !important;
		/* lololololololol */
	}

	.oauth-button {
		margin-bottom: 10px;
		opacity: 0.85;
		transition: opacity 0.15s;
	}

	.oauth-button:hover {
		opacity: 0.95;
		transition: opacity 0.15s;
	}

	.oauth-button:active {
		opacity: 1;
	}

	#google-oauth {
		font-size: larger;
		background-color: #ea4335;
	}

	#github-oauth {
		font-size: larger;
		background-color: #171515;
	}

	#discord-oauth {
		font-size: larger;
		background-color: #5865f2;
	}
</style>
"""