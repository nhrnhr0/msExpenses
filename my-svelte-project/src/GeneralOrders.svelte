<script>
    import Modal from 'svelte-simple-modal';
    import Content from './GeneralOrderEdit.svelte';

</script>
הזמנות:

<table>
    <th>
        תאריך
    </th>
    <th>
        תיאור רכישה
    </th>
    <th>
        ספק
    </th>
    <th>
        סכום
    </th>
    <th>
        סוג הוצאה
    </th>
    <th>
        פעולות
    </th>
</table>
<Modal>
    <Content/>
</Modal>


<style>
    table {
        width: 100%;
        border: 1px solid black;

        margin-bottom: 150px;
    }
    table th {
        border-bottom:2px solid black;
    }
</style>