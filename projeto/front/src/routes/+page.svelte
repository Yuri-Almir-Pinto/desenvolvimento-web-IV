<script>
	let menu = 1;
	import Movie from "./Movie.svelte"
	import Artista from "./Artist.svelte"
	import Nav from "./Nav.svelte"
</script>

<Nav bind:menu/>

<div class="card">
	{#if menu === 1}
		<Movie/>
	{:else if menu === 2}
		<Artista/>
	{:else if menu === 3}
		OPTION 3
	{:else}
		OPTION 4
	{/if}
</div>