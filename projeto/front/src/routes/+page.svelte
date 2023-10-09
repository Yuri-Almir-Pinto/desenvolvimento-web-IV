<script>
	let menu = 1;
	import Movie from "./Movie.svelte"
	import Artista from "./Artist.svelte"
	import Nav from "./Nav.svelte"
	import User from "./User.svelte"
</script>

<Nav bind:menu/>

<div class="card">
	{#if menu === 1}
		<Movie/>
	{:else if menu === 2}
		<Artista/>
	{:else if menu === 3}
		<User/>
	{:else}
		OPTION 4
	{/if}
</div>