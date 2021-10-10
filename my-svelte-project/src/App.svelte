<script>
	import {
		Tabs,
		Tab,
		TabList,
		TabPanel
	} from 'svelte-tabs';

	import GeneralOrders from './GeneralOrders.svelte'
</script>
<main>
	<Tabs>
		<TabList>
			<Tab>הזמנות כלליות</Tab>
			<Tab>Two</Tab>
			<Tab>Three</Tab>
		</TabList>

		<TabPanel>
			<GeneralOrders/>
		</TabPanel>

		<TabPanel>
			<h2>Panel Two</h2>
		</TabPanel>

		<TabPanel>
			<h2>Panel Three</h2>
		</TabPanel>
	</Tabs>
</main>
<style>
	:global(body) {
		direction: rtl;
	}
	:global(.svelte-tabs li.svelte-tabs__selected) {
		background-color: #eee;
	}
</style>