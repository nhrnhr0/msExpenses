<script>
	import 'chota';

	import GeneralOrders from './GeneralOrders/GeneralOrders.svelte'
	import ApprovedOrders from './ApprovedOrders/ApprovedOrders.svelte'
	import ArchivedOrders from './ArchivedOrders/ArchivedOrders.svelte';
	import { Tabs,Tab } from 'svelte-chota';

	let active_tab = window.sessionStorage.getItem('active_tab') || 0;
	$: {
		
		console.log('saving active tab to localStorage', active_tab);
		window.sessionStorage.setItem('active_tab', active_tab);
	}
	
</script>
<main>


	<Tabs full bind:active={active_tab}>
		<Tab>הזמנות כלליות</Tab>
		<Tab>הזמנות מאושרות</Tab>
		<Tab>הזמנות סגורות</Tab>
	</Tabs>

	{#if active_tab == 0}
		<h1>הזמנות כלליות</h1>
		<GeneralOrders/>
	{:else if active_tab == 1} 
		<h1>הזמנות מאושרות</h1>
		<ApprovedOrders/>
	{:else if active_tab == 2} 
		<h1>הזמנות סגורות</h1>
		<ArchivedOrders/>
	{/if}





<!--
	<Tabs>
		<TabList>
			<Tab on:click={tabClick}>הזמנות כלליות</Tab>
			<Tab>הזמנות מאושרות</Tab>
		</TabList>

		<TabPanel>
			<h1>הזמנות כלליות</h1>
			<GeneralOrders/>
		</TabPanel>

		<TabPanel>
			<h1>הזמנות מאושרות</h1>
			<ApprovedOrders/>
		</TabPanel>
	</Tabs>
	-->
</main>
<style>
	:global(body) {
		direction: rtl;
	}
	:global(.svelte-tabs li.svelte-tabs__selected) {
		background-color: #eee;
	}
	main {
		max-width: 100vw;
		overflow-x: hidden;
	}
</style>