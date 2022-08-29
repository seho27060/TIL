package com.practice.prac1.Domain;

import com.practice.prac1.Domain.DTO.MemberStageReqDTO;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;

@Entity
@Getter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class MemberStage {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "member_id")
    private Member member;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "stage_id")
    private Stage stage;

    private Long state; //해당 스테이지의 특정 멤버의 참여상태(참가중,완료 : 1,0)

    public void updateMemberStage(Long state){
        this.state = state;
    }
}
