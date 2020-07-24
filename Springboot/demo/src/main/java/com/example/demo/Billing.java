package com.example.demo;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class Billing {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;
	
	private Long billNum;
	
	private Long custNum;
	
	private String cashierID;

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public Long getBillNum() {
		return billNum;
	}

	public void setBillNum(Long billNum) {
		this.billNum = billNum;
	}

	public Long getCustNum() {
		return custNum;
	}

	public void setCustNum(Long custNum) {
		this.custNum = custNum;
	}

	public String getCashierID() {
		return cashierID;
	}

	public void setCashierID(String cashierID) {
		this.cashierID = cashierID;
	}
	
	
}
