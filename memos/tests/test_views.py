from django.test import TestCase
from django.urls import reverse
from memos.models import Memo

class MemoViewTests(TestCase):
    def test_list_page_ok(self):
        res = self.client.get(reverse("memo_list"))
        self.assertEqual(res.status_code, 200)

    def test_create_requires_title(self):
        res = self.client.post(reverse("create_memo"), data={"title": "", "body": "x", "tags": ""})
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "タイトルは必須")

    def test_memo_detail_returns_404_for_nonexistent_id(self):
        """Test that memo_detail returns 404 for non-existent memo ID"""
        res = self.client.get(reverse("memo_detail", args=[99999]))
        self.assertEqual(res.status_code, 404)

    def test_edit_memo_returns_404_for_nonexistent_id(self):
        """Test that edit_memo returns 404 for non-existent memo ID"""
        res = self.client.get(reverse("edit_memo", args=[99999]))
        self.assertEqual(res.status_code, 404)

    def test_memo_detail_works_with_existing_id(self):
        """Test that memo_detail works correctly with existing memo"""
        memo = Memo.objects.create(title="Test Memo", body="Test body")
        res = self.client.get(reverse("memo_detail", args=[memo.id]))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Test Memo")

    def test_edit_memo_works_with_existing_id(self):
        """Test that edit_memo works correctly with existing memo"""
        memo = Memo.objects.create(title="Test Memo", body="Test body")
        res = self.client.get(reverse("edit_memo", args=[memo.id]))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Test Memo")

    # TODO: detail/edit/delete / legacy検索 / pagination のテストを追加
