<script>
	let promise;
	async function getFilmes() {
    // faz um request GET para endpoint /filmes
		const res = await fetch(`http://localhost:8000/filmes/getMovieInfo`);
		const text = await res.json();
		if (res.ok) { return text; } 
    else { throw new Error(text);}
	}
	function handleClick() {
		promise = getFilmes();
	}
</script>

<button on:click={handleClick}> Get filmes </button>

{#await promise}
	<p>...waiting</p>
{:then filmes}
	{#if promise != null}
	<h1>Lista de filmes -</h1>
    {#each filmes as filme}
		<img src={filme.imagem} alt="Imagem do poster do filme">
		<p>{filme.nome}</p>
	{/each}
	{/if}
{:catch error}
	<p style="color: red">{error.message}</p>
{/await}

