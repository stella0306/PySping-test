// index.js

// 페이지 로딩 시 메모 목록을 받아와서 표시
window.onload = function() {
    fetch('/memos')  // Flask에서 JSON 데이터를 반환하는 URL
        .then(response => response.json())
        .then(data => {
            const memoList = document.getElementById('memoList');
            memoList.innerHTML = '';  // 기존 목록 초기화

            // 메모 데이터를 목록에 동적으로 추가
            data.forEach(memo => {
                const li = document.createElement('li');
                li.textContent = `${memo.title} - ${memo.content}`;
                memoList.appendChild(li);

                
                // 삭제 버튼 추가
                const deleteButton = document.createElement('button');
                deleteButton.textContent = '삭제';
                deleteButton.onclick = () => deleteMemo(memo.id);  // 메모 ID를 받아서 삭제 호출
                li.appendChild(deleteButton);

                memoList.appendChild(li);
            });
        })
        .catch(error => console.error('Error fetching memos:', error));
};

// 메모 추가 폼 제출 시 처리
document.getElementById('memoForm').addEventListener('submit', function(e) {
    e.preventDefault();  // 기본 제출 동작 방지

    const title = document.getElementById('title').value;
    const content = document.getElementById('content').value;

    // 메모 추가 요청 (POST)
    fetch('/memos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            title: title,
            content: content
        })
    })
    .then(response => response.json())
    .then(data => {
        // 새로운 메모가 추가되면 메모 목록을 갱신
        alert('메모가 추가되었습니다.');
        window.location.reload();  // 페이지를 새로 고쳐서 갱신된 목록 표시
    })
    .catch(error => console.error('Error adding memo:', error));
});


// 메모 삭제 함수
function deleteMemo(memoId) {
    if (confirm('정말로 이 메모를 삭제하시겠습니까?')) {
        fetch(`/memos/${memoId}`, {
            method: 'DELETE'
        })
        .then(response => {
            if (response.ok) {
                alert('메모가 삭제되었습니다.');
                window.location.reload();  // 삭제 후 페이지 새로고침
            } else {
                alert('삭제에 실패했습니다.');
            }
        })
        .catch(error => {
            console.error('Error deleting memo:', error);
            alert('삭제 중 오류가 발생했습니다.');
        });
}};