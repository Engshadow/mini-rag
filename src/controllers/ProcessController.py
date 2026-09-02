from .BaseController import BaseController
from .ProjectController import ProjectController
import os
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyMuPDFLoader
from models import ProcessEnums
from langchain_text_splitters import RecursiveCharacterTextSplitter


class ProcessController(BaseController):
    def __init__(self,project_id: str):
        super().__init__()

        self.project_id = project_id
        self.project_path = ProjectController().get_project_path(project_id=project_id)



    def get_file_extension(self, file_id: str):
        file_path = os.path.join(
            self.project_path,
            file_id
        )

        if not os.path.exists(file_path):
            return None

        _, file_extension = os.path.splitext(file_path)
        return file_extension
    def load_file(self, file_id: str):

        file_extension = self.get_file_extension(file_id=file_id)
        file_path = os.path.join(
            self.project_path,
            file_id
        )
        if file_extension == ProcessEnums.TXT.value:
            return TextLoader(file_path=file_path, encoding='utf-8')
        elif file_extension == ProcessEnums.PDF.value:
            return PyMuPDFLoader(file_path=file_path)
        return None

    def get_file_content(self, file_id: str):
        loader = self.load_file(file_id=file_id)
        if loader is None:
            return None
        return loader.load()

    def Process_file_content(self, file_content:list,chunk_size: int = 1000, chunk_overlap: int = 200):

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        file_content_text = [doc.page_content for doc in file_content]
        file_metadata = [doc.metadata for doc in file_content]
        chunks=text_splitter.create_documents(file_content_text ,metadatas=file_metadata)

        return chunks