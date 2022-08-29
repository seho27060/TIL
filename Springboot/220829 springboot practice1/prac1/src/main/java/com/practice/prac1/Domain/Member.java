package com.practice.prac1.Domain;

import com.practice.prac1.Domain.DTO.MemberReqDTO;
import com.practice.prac1.Domain.DTO.MemberResDTO;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
@Getter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Member {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    @OneToMany(mappedBy = "member", cascade = CascadeType.REMOVE)
    private List<MemberStage> memberStages;

    public void updateMember(MemberReqDTO memberReqDTO){
        this.name = memberReqDTO.getName();
    }
}
