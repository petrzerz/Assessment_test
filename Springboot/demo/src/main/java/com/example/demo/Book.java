package com.example.demo;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class Book {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;
	private Long bookid;
	private String bookName;
	private Long categoryID;
	private Long authorID;
	private Long publisher;
	public Long getId() {
		return id;
	}
	public void setId(Long id) {
		this.id = id;
	}
	public Long getBookid() {
		return bookid;
	}
	public void setBookid(Long bookid) {
		this.bookid = bookid;
	}
	public String getBookName() {
		return bookName;
	}
	public void setBookName(String bookName) {
		this.bookName = bookName;
	}
	public Long getCategoryID() {
		return categoryID;
	}
	public void setCategoryID(Long categoryID) {
		this.categoryID = categoryID;
	}
	public Long getAuthorID() {
		return authorID;
	}
	public void setAuthorID(Long authorID) {
		this.authorID = authorID;
	}
	public Long getPublisher() {
		return publisher;
	}
	public void setPublisher(Long publisher) {
		this.publisher = publisher;
	} 
	
	

}
