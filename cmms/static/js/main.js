function delete_item(){
	let isBoss = confirm("Если вы удалите, все зависимости будут удалены с данной таблицей, удалить ?");
	if (isBoss){
		document.getElementsByTagName('form')[0].method = 'DELETE'
		return true
	}
	return false
}