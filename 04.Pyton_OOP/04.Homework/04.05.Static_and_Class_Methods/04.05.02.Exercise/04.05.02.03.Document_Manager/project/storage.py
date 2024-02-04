from typing import List

from project import Category
from project import Document
from project import Topic


class Storage:
    def __init__(self) -> None:
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name:str) -> None:
        category = [c for c in self.categories if c.id == category_id][0]

        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        topic = [t for t in self.topics if t.id == topic_id][0]

        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = [d for d in self.documents if d.id == document_id][0]

        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = [c for c in self.categories if c.id == category_id][0]

        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = [t for t in self.topics if t.id == topic_id][0]

        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = [d for d in self.documents if d.id == document_id][0]

        self.documents.remove(document)

    def get_document(self, document_id):
        document = [d for d in self.documents if d.id == document_id][0]

        return document.__repr__()

    def __repr__(self):
        result = ""

        for doc in self.documents:
            result += f"{doc.__repr__()}\n"

        return result
